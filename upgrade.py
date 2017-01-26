# -*- coding: utf-8 -*-
from openerp.tools import config


def run(session, logger):
    """Update all modules."""
    if session.is_initialization:
        config['load_language'] = 'fr_FR'
        modules = [
            'zitcom',
        ]
        session.install_modules(modules)
        logger.info(
            "Fresh database ! Installing Zit com - modules: %r",
            modules
        )
        session.env.cr.commit()
        return
    logger.info("Default upgrade procedure : updating all modules.")
    session.update_modules(['all'])
