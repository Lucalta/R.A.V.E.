function startAnnotator(){
	jQuery(function(){
		
		var annotator = $('#mainContent').annotator().data('annotator');

		annotator.addPlugin('Permissions', {
			user: user
		});
		
		annotator.addPlugin('Store', {
			// The endpoint of the store on your server.
			prefix: '/annotate/' + page,

			// Attach the uri of the current page to all annotations to allow search.
			annotationData: {
				'uri': page
			},

			// This will perform a "search" action when the plugin loads. Will
			// request the last 20 annotations for the current url.
			// eg. /store/endpoint/search?limit=20&uri=http://this/document/only
			loadFromSearch: {
				'limit': 20,
				'uri': page
			},
			
			urls: {
				// These are the default URLs.
				create:  '/',
				update:  '/:id',
				destroy: '/:id',
				search:  '/'
			}
		})
		
	});
}