import starlight from '@astrojs/starlight';
import AstroPWA from '@vite-pwa/astro';
import { defineConfig, passthroughImageService } from 'astro/config';

import { manifest, seoConfig } from './src/utils/seoConfig';

export default defineConfig({
	site: 'https://rws-nl.github.io',
	base: 'rws-otl',
	integrations: [
		AstroPWA({
			mode: 'production',
			registerType: 'autoUpdate',
			manifest,
			workbox: {
				globDirectory: 'dist',
				globPatterns: ['**/*.{js,css,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico}'],
				navigateFallback: '/'
			},
			experimental: {
				directoryAndTrailingSlashHandler: true
			}
		}),
		starlight({
			favicon: '/favicon.ico',
			customCss: [
				'./src/styles/custom.css',
			],
			head: [
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Expires',
						content: '1y'
					}
				},
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Pragma',
						content: '1y'
					}
				},
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Content-Type',
						content: 'text/html; charset=UTF-8'
					}
				},
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Cache-Control',
						content: '1y'
					}
				},
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Page-Enter',
						content: 'RevealTrans(Duration=2.0,Transition=2)'
					}
				},
				{
					tag: 'meta',
					attrs: {
						httpEquiv: 'Page-Exit',
						content: 'RevealTrans(Duration=3.0,Transition=12)'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'apple-mobile-web-app-capable',
						content: 'yes'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'apple-mobile-web-app-capable',
						content: 'yes'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'apple-mobile-web-app-status-bar-style',
						content: 'black'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'apple-mobile-web-app-title',
						content: seoConfig.siteName
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'application-name',
						content: seoConfig.siteName
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'audience',
						content: 'all'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'author',
						content: `Rijkswaterstaat`
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'coverage',
						content: 'Worldwide'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'description',
						content: seoConfig.description
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'designer',
						content: `Rijkswaterstaat`
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'distribution',
						content: 'Global'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'googlebot',
						content: 'index,follow'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'HandheldFriendly',
						content: 'True'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'identifier-URL',
						content: seoConfig.baseURL
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'keywords',
						content: 'Rijkswaterstaat, OTL'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'owner',
						content: `Rijkswaterstaat`
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'rating',
						content: 'safe for kids'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'revisit-after',
						content: '7 days'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'robots',
						content: 'archive,follow,imageindex,index,odp,snippet,translate'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'shortlink',
						content: seoConfig.baseURL
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'subject',
						content: 'Documentatie website voor Rijkswaterstaat OTL'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'summary',
						content: seoConfig.description
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'target',
						content: 'all'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'theme-color',
						content: '#000000'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'twitter:card',
						content: 'summary'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'twitter:creator',
						content: '@rijkswaterstaat'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'twitter:site',
						content: '@rijkswaterstaat'
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'url',
						content: seoConfig.baseURL
					}
				},
				{
					tag: 'meta',
					attrs: {
						name: 'viewport',
						content: 'width=device-width, initial-scale=1'
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:description',
						content: seoConfig.description
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:locale',
						content: 'nl_NL'
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:site_name',
						content: seoConfig.siteName
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:title',
						content: seoConfig.siteName
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:type',
						content: 'website'
					}
				},
				{
					tag: 'meta',
					attrs: {
						property: 'og:url',
						content: seoConfig.baseURL
					}
				},
				{
					tag: 'link',
					attrs: {
						rel: 'canonical',
						href: seoConfig.baseURL
					}
				},
				{
					tag: 'link',
					attrs: {
						rel: 'icon',
						type: 'image/png',
						sizes: '192x192',
						href: '/android-chrome-192x192.png'
					}
				},
				{
					tag: 'link',
					attrs: {
						rel: 'icon',
						type: 'image/png',
						sizes: '512x512',
						href: '/favicon-512x512.png'
					}
				}
			],
			pagination: true,
			title: 'Rijkswaterstaat OTL',
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/RWS-NL/rws-otl'
				},
				{
					icon: 'twitter',
					label: 'Twitter',
					href: 'https://twitter.com/rijkswaterstaat'
				}
			]
		})
	],
	image: { service: passthroughImageService() }
});
