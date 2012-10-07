%import urllib
%artist = urllib.quote_plus(artist)
<ul data-role="listview" data-inset="true" data-filter="true" data-autodividers="true">
	%for album in albums:
		%enc_album = urllib.quote_plus(album)
	<li><a data-transition="slidefade" href="/tracks/{{artist}}/{{enc_album}}">{{album}}</a></li>
	%end
</ul>
%rebase layout backlink=backlink