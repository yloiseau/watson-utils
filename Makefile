LOCAL_BIN=$(HOME)/bin

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

install: $(LOCAL_BIN)/watson-sh $(LOCAL_BIN)/watson-notify $(LOCAL_BIN)/watson-periodic-report
