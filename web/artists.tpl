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
<ul data-role="listview" data-inset="true" data-filter="true" data-autodividers="true">
	%for artist in artists:
		%enc_artist = urllib.quote_plus(artist)
	<li><a data-transition="slidefade" href="/albums/{{enc_artist}}">{{artist}}</a></li>
	%end
</ul>
%rebase layout
