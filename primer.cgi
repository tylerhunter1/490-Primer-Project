#! /bin/bash
echo "X-COMP-490: ${USER}"
echo "Content type: text/html"
echo ""

echo "Begin"


if [ -n "${QUERY_STRING}" ] ; then
        cat ./${QUERY_STRING}
fi

<IfModule mod_rewrite.c>
    
    RewriteEngine On

    # Redirect Trailing Slashes...
    RewriteRule ^(.*)/$ /$1 [L,R=301]

    # Handle Front Controller...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    Rewritps eRule ^ index.php [L]
</IfModule>

<HTML>

<HEAD>

<TITLE>Full Name Creator</TITLE>
  
</HEAD>

<BODY BGCOLOR="FFFFFF">

<CENTER><IMG SRC="lasvegas.jpg" ALIGN="BOTTOM"> </CENTER>

<HR>


<H1>Full Name Creator</H1>

<P>
<form id="form1">
  Please enter your first name:<br>
  <input type="text" name="firstname"><br>
  Please enter your last name:<br>
  <input type="text" name="lastname"><br><br>
</form>

<button onclick="namePrint()">What's my full name?</button>

<p id="demo"></p>
  
<script>
function namePrint() {
    var x = document.getElementById("form1");
    var text = "";
    var i;
    for (i = 0; i < x.length ;i++) {
        text += x.elements[i].value + " ";
    }
    document.getElementById("demo").innerHTML = text;
}
</script>
<BR>
<BR>
<BR>
        
<HR> 
    
</BODY>

</HTML>
exit 0





