#! /bin/bash
echo "X-COMP-490: ${USER}"
echo "Content type: text/html"
echo ""

echo "Begin"


if [ -n "${QUERY_STRING}" ] ; then
        cat ./${QUERY_STRING}
fi


<HTML>

<HEAD>

<TITLE>Full Name Creator</TITLE>
  
</HEAD>

<BODY BGCOLOR="FFFFFF">

<CENTER><IMG SRC="lasvegas.jpg" ALIGN="BOTTOM"> </CENTER>

<HR>


<H1>Full Name Creator</H1>


<BR>
<BR>
<BR>
        
<HR> 
    
</BODY>

</HTML>
exit 0





