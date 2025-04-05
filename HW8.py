import datetime
import logging
logging.basicConfig(level= logging.INFO, filename="logs.log", filemode="w", format='%(asctime)s - %(levelname)s -%(message)s', datefmt="%d-%m-%Y")
date_now = not datetime.datetime.now().strftime("%d-%m-%Y")

logging.info(f"Error{date_now}")
