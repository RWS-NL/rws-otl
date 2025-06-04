import type { ManifestOptions } from 'vite-plugin-pwa';

const description = 'RWS OTL Viewer is de openbare Git repository van de Rijkswaterstaat Object Type Library';
const title = 'RWS OTL Viewer';

/**
 * Defines the default SEO configuration for the website.
 */
export const seoConfig = {
	baseURL: 'https://rws-nl.github.io/rws-otl',
	description,
	type: 'website',
	siteName: title,
	twitter: {
		card: 'summary_large_image',
		handle: '@rijkswaterstaat'
	}
};

/**
 * Defines the configuration for PWA webmanifest.
 */
export const manifest: Partial<ManifestOptions> = {
	name: title,
	short_name: title,
	description,
	theme_color: '#000000',
	background_color: '#ffffff',
	display: 'minimal-ui',
	dir: 'ltr',
	lang: 'nl_NL',
	orientation: 'portrait-primary',
	scope: '/',
	start_url: '/',
	"icons": [
		{
		  "src": "favicon.ico",
		  "sizes": "64x64 32x32 24x24 16x16",
		  "type": "image/x-icon"
		},
		{
		  "src": "android-chrome-192x192.png",
		  "sizes": "192x192",
		  "type": "image/png"
		},
		{
		  "src": "android-chrome-512x512.png",
		  "sizes": "512x512",
		  "type": "image/png"
		}
	  ],

};
