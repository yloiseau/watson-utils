
# Watson utilities

This is just some quick scripts to use with the wonderful [Watson](https://github.com/TailorDev/Watson) time tracker.

## `watson-sh`

An interactive shell for Watson. It simply dispatch to `watson` itself, but keep the context (current project, date span, …)
Use it with `rlwrap` (see `watson-sh --help`) for improved experience (command history, completion, …) 

## `watson-notify`

A cron script to alert you when you forgot to start Watson.

## `watson-monthly-report`

Print Watson reports by month.

## `watson-status`

An I3 bar status displaying the current project (using conky)

## `on-modify-watson.py`

A [Taskwarrior](http://taskwarrior.org/) hook to start a watson task according to a taskwarrior one.

## Licence

These scripts are released under the Do What The Fuck You Want To Public License
[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png)](http://www.wtfpl.net/)
