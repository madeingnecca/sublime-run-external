# Sublime Text 2 plugin: RunExternal

RunExternal executes the current selection as a shell command and replaces the selection with the output.

It supports multiple selections, so each selected region will be replaced with the output of the respective command.

<img style="display:block;margin:0 auto;" src="http://i.imgur.com/2dYAo.gif">

Developers can change a "command wrapper", a custom string used to construct the final command. For example cygwin users can use this as a command wrapper:

<pre>
'D:\\cygwin\\bin\\bash.exe --login -i -c "{0}"'
</pre>

Developers can also specify a timeout, used to limit in seconds the execution of a very long or even infinite command (e.g ping domain.com).

Checkout "RunExternal.sublime-settings" for these settings.

## Install

Clone this repository as RunExternal into your Packages directory.