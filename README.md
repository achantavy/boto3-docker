# boto3-docker

Demonstrates running boto3 scripts in a Docker container.

1. Ensure your AWS config is set properly on your host. This document assumes that your `~/.aws/config` file has entries that look like this:

	```
	[profile my-example-profile]
	role_arn = {the role to assume}
	region = {the region}
	credential_source = Environment
	[... etc ...]
	```

1. Build the Docker image.

	```
	cd /path/to/boto3-docker
	docker build . -t boto3-docker -f ./Dockerfile
	```

1. Set env var `PROFILE_NAME` to the name of the AWS profile you want the container to run as. For example to instruct the container to run as the example above, run

	```
	export PROFILE_NAME='my-example-profile'
	```

1. Run the test script within the container:

	```
	docker run -v $PWD/test:/app \
	           -v /path/to/.aws:/home/.aws/ \
	           -e PROFILE_NAME \
	           -e AWS_ACCESS_KEY_ID \
	           -e AWS_SECRET_ACCESS_KEY \
	           -e AWS_SESSION_TOKEN \
	           boto3-docker:latest python /app/test.py
	```

    Explanation

    * `-v $PWD/test:/app` mounts this project's `test/` folder to `/app` in the container

    * `-v /path/to/.aws:/home/.aws/` mounts your host's AWS files under `/path/to/.aws` to `/home/.aws` in the container. This is important because it ensures that your AWS `config` and `credentials` files (if you use them) are available to the container.

    	* Example: if your AWS `config` is located at `/Users/me/.aws/config`, use `-v /Users/me/.aws:/home/.aws/`.

    * The `-e` flags determine which enviroment variables on the host to make available to the container. In my testing, this is the minimum set of env vars to get this to work.

1. If it works, you will see the output of `ec2.describe_regions()`:

	```
	['eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2' ...
	```