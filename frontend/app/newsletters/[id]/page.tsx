'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import api from '@/utils/api';
import { Loader2, ArrowLeft } from 'lucide-react';

interface Newsletter {
    id: number;
    title: string;
    summary: string;
    content: string;
    sentiment: string;
    published_at: string;
}

export default function NewsletterDetailPage() {
    const params = useParams();
    const router = useRouter();
    const [newsletter, setNewsletter] = useState<Newsletter | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchNewsletter = async () => {
            try {
                const response = await api.get(`/newsletters/${params.id}`);
                setNewsletter(response.data);
            } catch (error) {
                console.error('Failed to fetch newsletter', error);
            } finally {
                setLoading(false);
            }
        };

        if (params.id) {
            fetchNewsletter();
        }
    }, [params.id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-[50vh]">
                <Loader2 className="animate-spin h-8 w-8 text-gray-400" />
            </div>
        );
    }

    if (!newsletter) {
        return (
            <div className="max-w-4xl mx-auto px-6 py-12 text-center">
                <h1 className="text-2xl font-bold mb-4">Newsletter Not Found</h1>
                <button
                    onClick={() => router.push('/newsletters')}
                    className="text-accent hover:underline"
                >
                    ← Back to Newsletters
                </button>
            </div>
        );
    }

    const date = new Date(newsletter.published_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });

    // Parse content and enriched data
    const delimiter = "Enriched Data:";
    const parts = newsletter.content.split(delimiter);
    const mainContent = parts[0];
    let sources: any[] = [];

    if (parts.length > 1) {
        try {
            const rawSources = parts[1].trim();

            // 1. Try standard JSON parse first (for new data or lucky old data)
            try {
                sources = JSON.parse(rawSources);
            } catch (jsonError) {
                // 2. If JSON fails, it's likely the Python string format: [{'key': 'value'}, ...]
                // We need a more robust regex-based extraction that handles:
                // - Mixed quotes (single or double)
                // - Python None/True/False
                // - Unsorted keys

                // Regex to match individual dictionary items in the list: { ... }
                // This non-greedy match finds each object block
                const objectRegex = /\{[^{}]+\}/g;
                let objectMatch;

                while ((objectMatch = objectRegex.exec(rawSources)) !== null) {
                    const objStr = objectMatch[0];
                    const sourceItem: any = {};

                    // Helper to extract field value regardless of quote type
                    const extractField = (fieldName: string) => {
                        // Matches: 'key': 'value' OR 'key': "value"
                        // Captures the quote used and the content
                        const fieldRegex = new RegExp(`'${fieldName}':\\s*(['"])(.*?)\\1`, 's');
                        const match = fieldRegex.exec(objStr);
                        return match ? match[2] : '';
                    };

                    sourceItem.title = extractField('title');
                    sourceItem.url = extractField('url');
                    sourceItem.snippet = extractField('snippet');

                    if (sourceItem.url) {
                        sources.push(sourceItem);
                    }
                }
            }
        } catch (e) {
            console.error("Failed to parse enriched data sources", e);
        }
    }

    return (
        <div className="max-w-7xl mx-auto px-6 py-12">
            <button
                onClick={() => router.push('/newsletters')}
                className="flex items-center gap-2 text-gray-400 hover:text-white mb-8 transition-colors group text-sm font-medium"
            >
                <ArrowLeft className="h-4 w-4 transition-transform duration-300 group-hover:-translate-x-1" />
                Back to Newsletters
            </button>

            {/* Split layout: 2 cols for article, 1 col for sources sidebar */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
                <div className="lg:col-span-2 space-y-8">
                    <article className="space-y-6">
                        <div className="flex items-center gap-4 text-xs font-semibold">
                            <span className="text-gray-500">{date}</span>
                            <span className={`px-3 py-1 rounded-full uppercase tracking-wider ${
                                newsletter.sentiment === 'Positive' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' :
                                newsletter.sentiment === 'Negative' ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20' :
                                'bg-indigo-500/10 text-indigo-400 border border-indigo-500/20'
                            }`}>
                                {newsletter.sentiment} Sentiment
                            </span>
                        </div>

                        <h1 className="text-3xl md:text-5xl font-extrabold text-white tracking-tight leading-tight">
                            {newsletter.title}
                        </h1>

                        {/* Glowing Summarizer Box */}
                        <div className="relative group p-6 rounded-2xl bg-primary/5 border border-primary/20 shadow-[0_0_30px_rgba(99,102,241,0.02)]">
                            <div className="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-primary to-accent rounded-l-2xl"></div>
                            <h3 className="text-xs font-bold uppercase tracking-widest text-primary mb-2">Executive AI Summary</h3>
                            <p className="text-gray-300 font-medium text-base md:text-lg leading-relaxed">
                                {newsletter.summary}
                            </p>
                        </div>

                        {/* Main Body */}
                        <div className="whitespace-pre-wrap text-gray-300 leading-relaxed text-base md:text-lg pt-4">
                            {mainContent}
                        </div>
                    </article>
                </div>

                {/* Sidebar Sources Column */}
                <div className="space-y-6 lg:border-l lg:border-white/5 lg:pl-10">
                    <div className="sticky top-28 space-y-6">
                        <div>
                            <h2 className="text-xl font-bold text-white mb-2">References & Reading</h2>
                            <p className="text-xs text-gray-400 leading-relaxed">
                                Curated web sources, discussion threads, and news records enriched automatically by our web agents.
                            </p>
                        </div>
                        
                        {sources.length > 0 ? (
                            <div className="space-y-4">
                                {sources.map((source, index) => (
                                    <a
                                        key={index}
                                        href={source.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="block p-4 rounded-xl glass-card border border-white/5 hover:border-primary/20 transition-all duration-300"
                                    >
                                        <h3 className="font-bold text-sm text-white line-clamp-2 mb-1 group-hover:text-primary transition-colors">
                                            {source.title}
                                        </h3>
                                        <p className="text-xs text-gray-400 line-clamp-3 mb-3 leading-relaxed">
                                            {source.snippet}
                                        </p>
                                        <span className="text-[11px] text-primary group-hover:text-white font-semibold flex items-center gap-1 transition-colors">
                                            Explore source →
                                        </span>
                                    </a>
                                ))}
                            </div>
                        ) : (
                            <div className="p-6 rounded-xl border border-white/5 text-center">
                                <p className="text-xs text-gray-500 font-medium">No verified source links attached to this edition.</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>

    );
}
