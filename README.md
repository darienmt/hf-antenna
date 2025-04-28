# hf-antenna
HF Antenna SWR data analysis

## Description

- [First installation and tunning](./EndfedAntenna.ipynb)
- [First installation per band](00-Installation.ipynb.ipynb)
- [Over tree installation per band](01-Installation.ipynb.ipynb)
- [SE HF-360 XP](03-Installation-SE-HF-360-XP.ipynb)
- [SE HF-360 XP with a choke](04-Installation-SE-HF-360-XP+Choke.ipynb)
- [SE HF-360 XP compared with end-fed and different configurations](SE-HF-360-XP-All.ipynb)

## Products

- [Professional End Fed Antenna for Outdoor, 4 Band 8 Band 1MHz to 30MHz 100W](https://www.amazon.ca/dp/B0CCLNJBM9)
- [SE HF-360 XP antenna at Amazon](https://www.amazon.ca/dp/B09TRQSQ3W)
- Choke above is [GRA-RWSM HH Antenna RF RFI Choke Coil Coax](https://www.amazon.ca/dp/B0CHRVBGH3)

## Development

### Create venv and install dependencies

```shell
python3 -m venv .venv
. ./.venv/bin/activate
python3 -m pip install -r ./requirements.txt
```

### Update Dependencies

```shell
python3 -m venv .venv
. ./.venv/bin/activate
python3 -m pip freeze > ./requirements.txt

```
