"""Create German Anki Cards."""
import argparse

from pyperclip import paste

from automating_anki.browser import getDriver, getTranslation, loadWordReference
from automating_anki.listener import listenForCopy
from automating_anki.note import Note


def main(word, driver):
    """Create a Anki card for the given word.

    Args:
        word: The word for which the note is being created.
        driver: The driver object for interacting with the web page.
    """
    note = Note("German Words and Grammar", word)

    loadWordReference(driver, word)

    note.setSentence(driver)
    note.setBack()
    getTranslation(driver, note.sentence)

    note.setDefinition(driver)
    getTranslation(driver, note.definition)

    note.setImage(driver)
    note.uploadNote()


def cli():
    """Command line interface to create German Anki cards."""
    parser = argparse.ArgumentParser(description="Create German Anki Cards.")
    parser.add_argument(
        "-r",
        required=False,
        action="store_true",
        default=False,
        help="Repeat the card creation process (t/F).",
    )

    parser.add_argument(
        "--word", default=paste(), help="Create Anki Card with this word."
    )

    args = parser.parse_args()

    try:
        # TODO: add option to edit card before continue
        # TODO: noun matching should handle capitals
        # TODO: add ability to select two words to blank out for
        #       separable verbs
        # TODO: select definition with number in Bedeutungen for
        #       WikitionaryParser, same for Sentences in Beispielen
        driver = getDriver()
        main(args.word, driver)
        while args.r:
            print("Copy the next word.\n")
            listenForCopy()
            main(paste(), driver)
    finally:
        driver.quit()
