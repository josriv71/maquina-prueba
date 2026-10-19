import pytest

from calculos import maximo, media


def test_media_de_tres():
    assert media([1, 2, 3]) == 2


def test_media_lista_vacia():
    with pytest.raises(ValueError):
        media([])


def test_maximo():
    assert maximo([3, 9, 4]) == 9
