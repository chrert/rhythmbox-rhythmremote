<!--
Copyright (c) 2012 Christian Ertler.
All rights reserved. This program and the accompanying materials
are made available under the terms of the GNU Public License v3.0
which accompanies this distribution, and is available at
http://www.gnu.org/licenses/gpl.html

Contributors:
    Christian Ertler - initial API and implementation
-->

%import urllib
%artist = urllib.quote_plus(artist)
<ul data-role="listview" data-inset="true" data-filter="true" data-autodividers="true">
	%for album in albums:
		%enc_album = urllib.quote_plus(album)
	<li><a data-transition="slidefade" href="/tracks/{{artist}}/{{enc_album}}">{{album}}</a></li>
	%end
</ul>
%rebase layout backlink=backlink
