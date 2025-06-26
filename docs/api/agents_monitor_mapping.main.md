# Module `agents_monitor_mapping.main`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `ensure_dir(path: str | pathlib.Path) -> pathlib.Path`

Ensure a directory exists, creating it if necessary.

Args:
    path (str | Path): The directory path to ensure.

Returns:
    Path: The resolved Path object of the directory.

Raises:
    OSError: If directory cannot be created due to permissions or other issues.

### `load_dotenv(dotenv_path: Union[str, ForwardRef('os.PathLike[str]'), NoneType] = None, stream: Optional[IO[str]] = None, verbose: bool = False, override: bool = False, interpolate: bool = True, encoding: Optional[str] = 'utf-8') -> bool`

Parse a .env file and then load all the variables found as environment variables.

Parameters:
    dotenv_path: Absolute or relative path to .env file.
    stream: Text stream (such as `io.StringIO`) with .env content, used if
        `dotenv_path` is `None`.
    verbose: Whether to output a warning the .env file is missing.
    override: Whether to override the system environment variables with the variables
        from the `.env` file.
    encoding: Encoding to be used to read the file.
Returns:
    Bool: True if at least one environment variable is set else False

If both `dotenv_path` and `stream` are `None`, `find_dotenv()` is used to find the
.env file with it's default parameters. If you need to change the default parameters
of `find_dotenv()`, you can explicitly call `find_dotenv()` and pass the result
to this function as `dotenv_path`.

### `main()`

Main function to run the mapping agent.
Expects config.yaml to include:
- storage_path
- report_path
- ocd_repo_url

### `today_utc_str() -> str`

Return today's date in UTC in 'YYYY-MM-DD' format.

Returns:
    str: Current UTC date as a string.

### `write_yaml(data: dict[str, typing.Any], path: str | pathlib.Path) -> pathlib.Path`

Write a dictionary to a YAML file.

Args:
    data (dict): Data to write.
    path (str | Path): File path to write to.

Returns:
    Path: The path the file was written to.
