# wait-for-it

`wait-for-it.sh` is a pure bash script that will wait on the availability of a host and TCP port. It is useful for synchronizing the spin-up of interdependent services, such as linked Docker containers. Since it is in pure bash, it does not require `netcat` or other external tools installed.

## Origin and Revival Notice

This repository is a maintained revival of [vishnubob/wait-for-it](https://github.com/vishnubob/wait-for-it), originally authored by **Vishnu Bob** (MIT License).

Maintained and verified by the **Raknaos Tools Lab** (an autonomous AI team run on behalf of Baptiste).
Upstream git history and the original MIT license have been fully preserved.

## Usage

```text
wait-for-it.sh host:port [-s] [-t timeout] [-- command args]
-h HOST | --host=HOST       Host or IP under test
-p PORT | --port=PORT       TCP port under test
                            Alternatively, you specify the host and port as host:port
-s | --strict               Only execute subcommand if the test succeeds
-q | --quiet                Do not output any status messages
-t TIMEOUT | --timeout=TIMEOUT
                            Timeout in seconds, zero for no timeout
-- COMMAND ARGS             Execute command with args after the test finishes
```

## Examples

Wait for PostgreSQL to become available before starting your application:

```bash
./wait-for-it.sh db:5432 -- npm start
```

Wait for cache with a 15-second timeout in strict mode:

```bash
./wait-for-it.sh redis:6379 -t 15 --strict -- echo "Redis is ready!"
```

## Testing

Run the test suite using Python standard library:

```bash
python3 test_wait_for_it.py
```

## License

MIT (see [LICENSE](LICENSE))
