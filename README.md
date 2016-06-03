
# Watson utilities

These are just some quick scripts to use with the wonderful [Watson](https://github.com/TailorDev/Watson) time tracker.

## `watson-sh`

An interactive shell for Watson. It simply dispatches to `watson` itself, but keeps the context (current project, date span, …)
Use it with `rlwrap` (see `watson-sh --help`) for improved experience (command history, completion, …) 

Optional dependency:
- `rlwrap`

## `watson-notify`

A cron script to alert you when you forgot to start Watson.
Displays a notification when:
- you are working on the same project for a long period,
- you are not working on a project.

The purpose is to remind you to start tracking your time, or to check if you
have forgotten to change the project (and remind you to take a break).

Uses `notify-send` (from `libnotify`) to send the alert.

Put the script in a `cron` task. For instance:

    */5 *  *   *   *     $HOME/bin/watson-notify

You can redefined the alert parameters in the `$WATSON_DIR/alert` file which will be sourced if present. Run `watson-notify -c` to display the current configuration.

    watson-notify -c > $HOME/.config/watson/alert

TIP: to use a random message, put one message by line in a file (e.g. `$HOME/.config/watson/messages`)
and use

    QUESTION_MESSAGE="$(shuf -n 1 $CONFIG_DIR/messages)"

in the `$WATSON_DIR/alert` file.

Dependency:
- `notify-send`: (`libnotify-bin` on Debian)


## `watson-periodic-report`

Print Watson reports by time periods.

This is just a little wrapper around `watson report`. For instance, 
to print a monthly report for the last 5 months:

    watson-periodic-report 5 months

and to print a weekly report for the last 10 weeks

    watson-periodic-report 10 weeks


## `watson-status`

An [I3](http://i3wm.org/) bar status displaying the current project (using [conky](https://github.com/brndnmtthws/conky)). 

Save in e.g. `~/.config/i3/watson-status` and add

    {"full_text": "\${texeci 5 ~/.config/i3/watson-status}"}

to your conky configuration file.


## `on-modify-watson.py`

A [Taskwarrior](http://taskwarrior.org/) hook to start a watson task according to a taskwarrior one.

When starting a task in taskwarrior, the hook starts a corresponding project in
watson. The project and keywords of the taskwarrior task are used in watson.
When stopping a task in taskwarrior, the hook stops the watson project.

To install, copy in `$HOME/.task/hooks/on-modify-watson.py` and make executable.


## Licence

These scripts are released under the Do What The Fuck You Want To Public License.

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png)](http://www.wtfpl.net/)
