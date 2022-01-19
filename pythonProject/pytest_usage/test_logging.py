import logging

def test_loggingDemo():

    # __name__ will capture your filename so that its easy to know from which file you are getting log
    logger = logging.getLogger(__name__)

    # this is to create file for logging so we need filehandler
    fileHandler = logging.FileHandler('log1file.log')
    # in which format we need to print
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    # '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    # setting connection between formatter to filehandler so that once filehandler is ther it will do both
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    # this is the order if you set level to warning then it will skip debug and info and only print warning error and critical

    #logger.setLevel(logging.INFO)
    logger.debug("A debug statmet is executed")
    logger.info("information statement ")
    logger.warning("Some thinh in Warning")
    logger.error(" this is an error essage")
    logger.critical(" some tihing critical happend ")

    # create a class and put this in class and cll in each file