<!--
Copyright (c) 2012 Christian Ertler.
All rights reserved. This program and the accompanying materials
are made available under the terms of the GNU Public License v3.0
which accompanies this distribution, and is available at
http://www.gnu.org/licenses/gpl.html

Contributors:
    Christian Ertler - initial API and implementation
-->

<ul data-role="listview" data-inset="true" data-filter="true">
	%for track in tracks:
	<li><a class="playlist_play_link" data-rb-entry-id="{{track[0]}}" data-rb-playlist-name="{{playlist}}" href="#">{{track[1]}}</a></li>
	%end
</ul>
%rebase layout backlink=backlink
