%import urllib
<ul data-role="listview" data-inset="true" data-filter="true" data-autodividers="true">
	%for artist in artists:
		%enc_artist = urllib.quote_plus(artist)
	<li><a data-transition="slidefade" href="/albums/{{enc_artist}}">{{artist}}</a></li>
	%end
</ul>
%rebase layout