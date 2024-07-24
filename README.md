# Guild Item Level Report

A simple Python script originally created in June 2022 for Mistblade 1, made to fetch guild information from the Stormforge API and list all players in a guild, sorted by their item level.

## Features

- Fetches guild data from the Stormforge API.
- Retrieves and calculates player item levels.
- Sorts players by their item level in descending order.

## Installation

1. **Clone the Repository** (if applicable):
    ```bash
    git clone https://github.com/mv-27/guild_ilvl_report.git
    cd guild_ilvl_report
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.6 or higher installed. Then, install the required Python library:
    ```bash
    pip install requests
    ```

## Configuration

Update the script’s configuration section with your API credentials:

- **API_KEY**: Your API key for accessing the Stormforge API.
- **SECRET_KEY**: Your secret key for API authentication.

## Usage

Run the script using Python and specify the realm and guild names with `--realm` and `--guild` options:

```bash
python ilvl_report.py --realm <realm_name> --guild <guild_name>
```

Replace `<realm_name>` (e.g. 'Mistblade') and `<guild_name>` with the actual names of the realm and guild you want to query.

The script will output a list of guild members sorted by item level.

## Example Output

```
1. :warrior: PlayerOne - 475 ilvl
2. :mage~1: PlayerTwo - 470 ilvl
3. :druid: PlayerThree - 465 ilvl
```

## Script Details

- **TauriAPI_Request(url, params)**: Sends a POST request to the Stormforge API and returns the JSON response.
- **FindItemLevel(name, realm)**: Retrieves and calculates the average item level of a character.
- **ListGuildItemLevels(realm, guild_name)**: Lists guild members sorted by item level and prints the result.

## Notes

- Replace placeholders in the configuration section with actual values.
- Ensure you have valid API credentials to access the Stormforge API.
- The script requires an internet connection to fetch data from the API.