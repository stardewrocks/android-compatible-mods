//export a GET request handler, that takes the ?url= query parameter and returns the contents of the file at that URL.
//this is svelte +server.ts btw

import { json } from '@sveltejs/kit';

export async function GET({ request, params, url }) {
    let parameters = url.searchParams;
    
    let urlToFetch = parameters.get('url');
    let urlToFetchValidRegex = /https\:\/\/smapi\.io\/log\/[a-zA-Z0-9]{32}/;

    if (!urlToFetch) return json({ error: 'No/invalid URL provided' });

    let response = await fetch(urlToFetch);

    if (!response.ok) return json({ error: 'Could not fetch URL' });

    let text = await response.text();

    return json({ text });
}