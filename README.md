# Monitoring

## Introduction

C'est une application de monitoring qui permet de surveiller certaines données de votre machine linux.

## Fonctionnalités

Voici une liste des fonctionnalité presente dans l'application :

- Check le pourcentage d'utilisation du CPU et de la RAM
- Check le pourcentage de stockage utilisé sur le disque
- Check si une liste de ports est ouvert
- Création de rapport à la fin de chaque check
- Rapport automatique toutes les 10 minutes
- Alertes Discord en cas d'un pourcentage trop élevé
- API pour visualiser tout les rapports

## Prérequis

Avoir une machine avec une distribution linux basée sur Red Hat et avoir git installé sur votre machine.

## Installation et Configuration

Pour pouvoir installer et configurer l'application veuillez suivre précisément ces instructions :

- Clonez le repo sur votre machine :
```shell
git clone https://github.com/Lytzeer/Monit
```

- Déplacez vous dans le dossier Monit du répo :
```shell
cd Monit/
```

- Configurez les 3 fichiers de conf :
```shell
# Configuration Ip machine et ports à surveiller
nano conf/conf.json 

# Configuration Ip et port de l'API
nano conf/api_conf.json

# Configuration Webhook Discord
nano conf/alerts.json
```

- Initiez l'application :
```
chmod +x init.sh
sudo ./init.sh
```

A partir de maintenant un rapport sera généré toutes les 10 minutes.

## Utilisation

Vous pouvez accéder à l'API depuis l'ip et le port que vous avez indiqué dans le fichier de conf correspondant pendant l'installation, vous y trouverez la documentation de l'API.

## Crédit

Application réalisé par [Lytzeer](https://github.com/Lytzeer)
