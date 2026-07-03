debt
====

Application bureau de **gestion des dettes, créanciers et remboursements**.

Interface graphique PyQt4 pour suivre qui vous doit de l'argent, enregistrer les paiements et visualiser les alertes sur le tableau de bord.

Fonctionnalités
---------------

- Gestion des créanciers (nom, prénom, adresse, téléphone)
- Enregistrement des dettes avec montant et dates
- Suivi des opérations de paiement par dette
- Tableau de bord avec alertes
- Interface en français (gettext)
- Packaging Windows (py2exe + NSIS)

Stack technique
---------------

- Python 2 · PyQt4
- SQLAlchemy · SQLite
- ReportLab · xlwt

Installation
------------

.. code-block:: bash

   pip install SQLAlchemy pysqlite
   python debt/maindebt.py

Build Windows
-------------

.. code-block:: bash

   python debt/setup-win.py py2exe

Auteur
------

`Ibrahima Fadiga <https://github.com/fadiga>`_ — Bamako, Mali
