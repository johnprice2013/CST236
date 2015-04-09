Source Example
==============

Source2 provides functions for describing a quadrilateral.

Determining Quadrilateral Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_quadrilateral_type` provides users with a way to provide a set of four sides
of a quadrilateral and returns the type of quadrilateral ("rectangle", "square", "rhombus" or "invalid")

Rectangle Example
^^^^^^^^^^^^^^^^^

>>> from source.source2 import get_quadrilateral_type
>>> get_quadrilateral_type(1, 1, 2, 2)
'rectangle'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: