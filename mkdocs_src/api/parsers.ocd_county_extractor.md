# Module `parsers.ocd_county_extractor`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `extract_counties(storage_path: str | pathlib.Path, config: dict) -> pandas.core.frame.DataFrame`

Extract county-level OCD identifiers and build a scaffold DataFrame.

Args:
    storage_path (str | Path): Root path to today's storage folder.
    config (dict): Config dictionary (unused but accepted for consistency).

Returns:
    pd.DataFrame: County scaffold with ocd_id, state, county_slug, and empty OpenStates column.

### `extract_county_slug(ocd_id: str) -> str`

Extract the county slug (lowercase, underscore form) from an OCD division ID.

Example:
    'ocd-division/country:us/state:mn/county:st_louis' -> 'st_louis'

### `extract_state_code(ocd_id: str) -> str`

Extract the state code from an OCD division ID.

Example:
    'ocd-division/country:us/state:mn/county:st_louis' -> 'mn'
