.PHONY: clean generate

clean:
	@echo "Removing old files"
	rm *.log
	rm models.html

generate:
	@echo "Creating new PyDoc and Models files"
	pydoc -w models
	git log --pretty=format:'%h : %s' --graph > IDB3.log

	
	
