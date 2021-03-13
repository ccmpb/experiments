ALGO=rsa4096
UID="Colin Campbell (keyflow) <colin@elusivelabs.com"
EXPIRE=1y

FPR = $(shell gpg -k --with-colons $(UID) | grep "^fpr" | head -n1 | cut -d: -f10)

new:
	@echo "Generating new gpg key."
	gpg --quick-generate-key $(UID) $(ALGO) default $(EXPIRE) 

add:
	@echo "Generating new gpg sub key on $(FPR)"
	gpg --quick-add-key $(FPR) $(ALGO)
	# gpg --quick-add-key $(KEYID) $(ALGORITHM_SUB) encr $(EXPIRE)
export:
	gpg --armor --export $(UID) 

show:
	gpg --list-keys
