import logging
import os
import sys
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lH = logging.StreamHandler(sys.stdout)
# lH.setLevel(logging.INFO)
lH.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'))

# lE = logging.StreamHandler(sys.stderr)
# lE.setLevel(logging.ERROR)
# lE.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'))

logger.addHandler(lH)
# logger.addHandler(lE)

while True:
    logger.info("testing info masuk mana nih")
    logger.error("testing error masuk mana nih")
    logger.debug("testing debug masuk mana nih")
    time.sleep(3.0)