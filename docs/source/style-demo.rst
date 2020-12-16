Demo Page
=========

Sub-Section Title
-----------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris auctor lorem non ligula dapibus, a dapibus tortor volutpat. Donec fringilla magna enim. Etiam interdum hendrerit ante vel ullamcorper. Pellentesque ultrices dui ligula, sed posuere diam facilisis laoreet. Vestibulum gravida consequat tortor eget rhoncus. Duis quis libero vel erat congue interdum. 

Morbi pretium arcu ut risus molestie, id eleifend eros dapibus. Nunc eget orci non lorem tincidunt dignissim. Integer vel quam nisi. Nunc sollicitudin massa eu sem mattis fermentum. Donec fringilla faucibus mauris quis luctus. Proin ac turpis pulvinar, rhoncus erat tempus, molestie diam. Cras non bibendum elit, id dictum arcu.

Sub-Sub-Section Title
^^^^^^^^^^^^^^^^^^^^^

Morbi pretium arcu ut risus molestie, id eleifend eros dapibus. Nunc eget orci non lorem tincidunt dignissim. Integer vel quam nisi. Nunc sollicitudin massa eu sem mattis fermentum. Donec fringilla faucibus mauris quis luctus. Proin ac turpis pulvinar, rhoncus erat tempus, molestie diam. Cras non bibendum elit, id dictum arcu. Nunc velit enim, posuere consectetur felis et, iaculis pellentesque est. Vivamus id facilisis est. Praesent tortor lacus, mattis at neque in, gravida pulvinar ex. Praesent ut ligula quis orci pretium molestie. Phasellus neque ex, viverra imperdiet feugiat in, convallis et nibh.

**The divider between Sub-setions:**

-----------------------

Images and Figures
--------------------

Image
   This is an image with no caption.

   .. image:: _static/img/qgis310.png 
      :align: center

Figure
   This is a figure, an image plus a caption. Use always with images describing processing steps or activities and add a meaningful caption.
   A reference to the figure looks like this :numref:`figquerysimple`.
   
   .. _mylabel:
   .. figure:: _static/img/task-simple-query.png
      :alt: simple query
      :figclass: align-center

      This the caption for this figure without a period

In-line Image
   In-line images are useful to show buttons and icons of a GUI inside a piece of text, such as a save button |saveEdits|


-----------------

Tables
------

**A table with spaning.**

   +------------+--------------+-----------+
   | Header 1   | Header 2     | Header 3  |
   +============+==============+===========+
   | body row 1 | spanning over two columns|
   +------------+--------------+-----------+
   | \          | <-empty cell | column 3  |
   +------------+--------------+-----------+


**A table without spaning.**

   =============  =============  =============  
   Header 1       Header 2       Header 3 
   =============  =============  =============
   row content     row content   row content
   another row     followed by   empty row
   \                \            \
   more rows       more rows     more row    
   =============  =============  ============= 

--------------------------------

Lists 
-----

Unnumbered Lists
   + Firts item.
   + Second item.
   + More items.
   

Numbered Lists
   1. Firts item.
   2. Second item.
   3. Third item.

---------------------

Hyperlinks
----------

+ This is a **text hyperlink** to `QGIS Home Page. <https://qgis.org/en/site/>`_
+ This is a hyperlink with a download icon :download:`file.zip <_static/img/qgis310.png>`
+ This is how a link to a concept in the LTB looks like: |ltb| `Concept name <#>`_



Especial Content
----------------

.. note:: 
   **QGIS.**
   Specific functionality or info about QGIS.

.. note:: 
   **Reflection.**
   Important concept or question, take some time to think about it.  

.. important:: 
   **Resources.**
   Text including a link to download the `dataset.zip <#>`_.

   If relevant an unnumbered list of files or datasets, such as:

   + ``dataset-1.ext`` - A short description.
   + ``data-file.ext`` - A description.

.. attention:: 
   **Question.**
   A question or a list of questions.

-----------------------

QGIS Icons
----------

See https://docs.qgis.org/3.10/en/docs/documentation_guidelines/substitutions.html 


-------------------------

Video Content
-------------
An embedded video from Vimeo:

.. raw:: html

   <div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/313813125?color=007e83&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

----------------------------

Text Formatting Examples
------------------------

=============================================   ==================================================   
Content                                         Style                                              
=============================================   ==================================================   
Filename + extension                             ``filename.ext``
*Data* layer or filename without extension       *'name-data-layer'* or *'filename'*
Tool name                                        **tool name**
Action on sofware interface                     Go to :guilabel:`Menu` > :guilabel:`Save`                                                                                              
Inline math expression                          The value of :math:`\pi = 3.14159`

Inline scalar (magnitude unit)                  A distance of  :math:`100 \ m`    
Inline equation or math expression              A theorem :math:`c^2 = \sqrt{a^2 + b^2}`. 
Equation                                        The same theorem as stand alone equation:                                                         
                                                
                                                .. math::

                                                   c^2 = \sqrt{a^2 + b^2}            
Code block (any language)                       An SQL expression with line numbers:
                                                                                                         
                                                .. code-block:: postgresql
                                                   :linenos:

                                                   SELECT *
                                                   FROM my_table
                                                   WHERE my_condition == True

Inline code                                     A python expression :code:`>>> x = 10 + 2`        
=============================================   ==================================================  
