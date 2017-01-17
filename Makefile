LOCAL_BIN=$(HOME)/bin
TASKDATA ?= $(HOME)/.local/share/task
TASK_HOOKS=$(TASKDATA)/hooks
I3_CONFIG=$(HOME)/.config/i3

ALL_FILES = \
    $(LOCAL_BIN)/watson-sh \
    $(LOCAL_BIN)/watson-notify \
    $(LOCAL_BIN)/watson-convert \
    $(LOCAL_BIN)/watson-periodic-report \
    $(TASK_HOOKS)/on-modify-watson.py \
    $(I3_CONFIG)/watson-status

check_watson:
	@which watson > /dev/null && echo "watson \033[32mOK\033[00m" || echo "watson \033[31mNOT FOUND\033[00m"

check_rlwrap:
	@which rlwrap > /dev/null && echo "rlwrap \033[32mOK\033[00m" || echo "rlwrap \033[33mNOT FOUND\033[00m"

check_notify:
	@which notify-send > /dev/null && echo "notify-send \033[32mOK\033[00m" || echo "notify-send \033[31mNOT FOUND\033[00m"

check_task:
	@which task > /dev/null && echo "task \033[32mOK\033[00m" || echo "task \033[31mNOT FOUND\033[00m"

check: check_watson check_notify check_rlwrap check_task

$(LOCAL_BIN)/%: %
	@echo "Install $< to $@"
	@install -m 555 $< $@

install: $(ALL_FILES)

$(TASK_HOOKS)/on-modify-watson.py: on-modify-watson.py
	@echo "Install $< to $@"
	@install -m 555 $< $@

$(I3_CONFIG)/watson-status: watson-status
	@echo "Install $< to $@"
	@install -m 555 $< $@

