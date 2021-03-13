ALGO=rsa4096
UID="Colin Campbell (keyflow) <colin@elusivelabs.com>"
EXPIRE=1y

FPR = $(shell gpg -k --with-colons $(UID) | grep "^fpr" | head -n1 | cut -d: -f10)

generate:
	gpg --quick-generate-key $(UID) $(ALGO) default never

delete:
	gpg --batch --delete-secret-keys $(FPR) 
	gpg --batch --delete-keys $(FPR)

add:
	gpg --quick-add-key $(FPR) $(ALGO)
	# gpg --quick-add-key $(KEYID) $(ALGORITHM_SUB) encr $(EXPIRE)
export:
	gpg --armor --export $(UID) 

show:
	gpg --list-keys
