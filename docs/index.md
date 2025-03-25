# App Photographe

Créer un dossier `artefacts` puis dans ce dossier un dossier `totreat`  
Placer dans ce dernier les photos elles-mêmes dans des sous-dossiers.

Ouvrir un terminal puis exécuter la commande suivante :

Avant de lancer le traitement, il est nécessaire que gsutil soit installé et configuré.

```shell
sudo snap install google-cloud-sdk
gcloud auth login
```

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd src
python3 treat.py
```

Le triage des photos est réalisé par streamlit.

```shell
cd streamlit
streamlit run triage.py
```