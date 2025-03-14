

.PHONY: test clean

test:
	@echo "Running tests..."
	@python3 -m pytest test
	
clean:
	@echo "Cleaning up..."	
	@rm -rf */__pycache__/
