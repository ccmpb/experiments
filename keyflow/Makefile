ALGO=rsa4096
ID="Colin Campbell (keyflow) <colin@elusivelabs.com"
EXPIRE=1y

new:
	@echo "Generating new gpg key ."
	gpg --quick-generate-key $(ID) $(ALGO) default $(EXPIRE) 

show:
	gpg --list-keys
