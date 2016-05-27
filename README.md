
# Watson utilities

This is just some quick scripts to use with the wonderful [Watson](https://github.com/TailorDev/Watson) time tracker.

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

Dependency:
- `notify-send`: (libnotify-bin on Debian)


## `watson-periodic-report`

Print Watson reports by time periods.

## `watson-status`

An I3 bar status displaying the current project (using conky)

## `on-modify-watson.py`

A [Taskwarrior](http://taskwarrior.org/) hook to start a watson task according to a taskwarrior one.

## Licence

These scripts are released under the Do What The Fuck You Want To Public License
[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png)](http://www.wtfpl.net/)
