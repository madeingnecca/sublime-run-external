import sublime, sublime_plugin
import subprocess, threading

class RunExternalCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        
        view = self.view
        settings = sublime.load_settings('RunExternal.sublime-settings')

        command_wrapper = settings.get('command_wrapper', '{0}')
        timeout = settings.get('timeout', 5)

        for region in view.sel():
            command = view.substr(region).encode('utf-8')
            command = command_wrapper.format(command)

            executer = RunExternalThread(command)
            executer.start()
            executer.join(timeout)

            if executer.isAlive():
                executer.kill()
                executer.error = '"{0}" killed after {1} seconds'.format(command, timeout)

            if executer.error:
                sublime.error_message(executer.error.decode('utf-8'))
            else:
                view.replace(edit, region, executer.output.decode('utf-8'))

class RunExternalThread(threading.Thread):

    command = None
    output = None
    error = None
    process = None

    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command

    def run(self):
        self.process = subprocess.Popen(
            self.command,
            shell = True,
            bufsize = -1,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            stdin = subprocess.PIPE)

        self.output, self.error = self.process.communicate()

    def kill(self):
        self.process.kill()