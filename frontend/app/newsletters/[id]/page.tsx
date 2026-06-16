'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import api from '@/utils/api';
import { Loader2, ArrowLeft, Twitter, MessageSquare, Globe, ArrowUpRight, TrendingUp, Sparkles, Clock, Share2, Bookmark } from 'lucide-react';
import Link from 'next/link';

interface Newsletter {
    id: number;
    title: string;
    summary: string;
    content: string;
    sentiment: string;
    published_at: string;
}

interface Source {
    title: string;
    url: string;
    snippet: string;
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
                <Loader2 className="animate-spin h-8 w-8 text-primary" />
            </div>
        );
    }

    if (!newsletter) {
        return (
            <div className="max-w-4xl mx-auto px-6 py-12 text-center text-on-background">
                <h1 className="text-2xl font-bold mb-4">Newsletter Not Found</h1>
                <button
                    onClick={() => router.push('/newsletters')}
                    className="text-primary hover:underline font-semibold"
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
    let sources: Source[] = [];

    if (parts.length > 1) {
        try {
            const rawSources = parts[1].trim();

            // Try standard JSON parse first
            try {
                sources = JSON.parse(rawSources);
            } catch (jsonError) {
                // If JSON fails, fall back to regex python parsing
                const objectRegex = /\{[^{}]+\}/g;
                let objectMatch;

                while ((objectMatch = objectRegex.exec(rawSources)) !== null) {
                    const objStr = objectMatch[0];
                    const sourceItem: any = {};

                    const extractField = (fieldName: string) => {
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

    // Determine reader score and impact based on sentiment
    let sentimentScore = "68.2%";
    let sentimentColor = "text-primary";
    if (newsletter.sentiment === 'Positive') {
        sentimentScore = "94.8%";
        sentimentColor = "text-emerald-600";
    } else if (newsletter.sentiment === 'Negative') {
        sentimentScore = "24.3%";
        sentimentColor = "text-rose-600";
    }

    // Categorize sources for custom layout styling
    const getSourceType = (url: string) => {
        const lowerUrl = url.toLowerCase();
        if (lowerUrl.includes('twitter.com') || lowerUrl.includes('x.com')) return 'twitter';
        if (lowerUrl.includes('reddit.com')) return 'reddit';
        return 'news';
    };

    return (
        <main className="max-w-container-max-width mx-auto px-margin-mobile md:px-margin-desktop py-12 text-on-background">
            <button
                onClick={() => router.push('/newsletters')}
                className="flex items-center gap-2 text-on-surface-variant hover:text-primary mb-8 transition-colors group text-label-bold"
            >
                <ArrowLeft className="h-4 w-4 transition-transform duration-300 group-hover:-translate-x-1" />
                Back to Newsletters
            </button>

            {/* Split layout */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
                
                {/* Main Content Area */}
                <article className="lg:col-span-8 space-y-12">
                    
                    {/* Header Section */}
                    <header className="space-y-6">
                        <div className="flex items-center gap-3">
                            <span className="bg-primary-container text-on-primary-container px-3 py-1 rounded-full font-sans text-caption font-bold">
                                VOL. {newsletter.id} • AI PULSE
                            </span>
                            <span className="text-on-surface-variant font-sans text-caption">
                                {date.toUpperCase()}
                            </span>
                        </div>
                        <h1 className="font-display text-display-xl text-on-background">
                            {newsletter.title}
                        </h1>
                        <div className="flex items-center gap-4 py-4 border-y border-outline-variant">
                            <div className="w-12 h-12 rounded-full bg-primary-container/30 flex items-center justify-center font-display font-bold text-primary text-headline-md border border-primary-container">
                                AI
                            </div>
                            <div>
                                <p className="font-sans text-label-bold text-on-background">Agent System</p>
                                <p className="font-sans text-caption text-on-surface-variant">Automated Ingestion & Enrichment Pipeline</p>
                            </div>
                            <div className="ml-auto flex gap-2">
                                <button className="p-2 rounded-full hover:bg-surface-container-high transition-colors text-primary">
                                    <Bookmark className="h-5 w-5" />
                                </button>
                                <button className="p-2 rounded-full hover:bg-surface-container-high transition-colors text-primary">
                                    <Share2 className="h-5 w-5" />
                                </button>
                            </div>
                        </div>
                    </header>

                    {/* Executive AI Summary Box */}
                    <section className="bg-surface-container-lowest border-2 border-primary-container rounded-xl p-8 glow-yellow relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-4 opacity-10">
                            <Sparkles className="h-20 w-20 text-primary" />
                        </div>
                        <div className="flex items-center gap-2 mb-4">
                            <span className="h-2 w-2 rounded-full bg-primary animate-pulse"></span>
                            <h2 className="font-sans text-label-bold uppercase text-primary">
                                Executive AI Summary
                            </h2>
                        </div>
                        <p className="font-sans text-body-lg text-on-background leading-relaxed">
                            {newsletter.summary}
                        </p>
                    </section>

                    {/* Conceptual routing illustration */}
                    <div className="my-10 bg-surface-container-low rounded-2xl overflow-hidden border border-outline-variant group">
                        <img 
                            src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvMarKSpRG9lCWlvHcxJO2bTKcC9pSjbOnunLVxCN3VTTx3cDlLSxhClr0on3F-W75QJ0X5ykdVJmBJKq_cng9LrO84vSRnjGV7FLfDNXjX71rAKpOMESTdrH3A1ETEpKol5c0FhLz5HqwRdzhZNkXqML1l7ejhMJZc0_ojwNnQaGsKbSrKtzmHP2w_d441hwbvOYyWcTiZ7zhjCWWmmDmLmTEztudA9dMNiem-rC1fkcIa7qyqcp0DQPccnazXCGeL1_oxHb_4JY" 
                            alt="Multi-agent neural routing pathways illustration" 
                            className="w-full h-[360px] object-cover group-hover:scale-105 transition-transform duration-700"
                        />
                        <div className="p-4 text-center italic font-sans text-caption text-on-surface-variant font-semibold">
                            Fig 1.1: Visualization of multi-agent neural routing paths in a production environment.
                        </div>
                    </div>

                    {/* Main Body content */}
                    <div className="whitespace-pre-wrap font-sans text-body-lg text-on-background leading-relaxed space-y-6 pt-4">
                        {mainContent}
                    </div>

                    {/* Footer Action Card */}
                    <div className="bg-inverse-surface text-inverse-on-surface rounded-2xl p-10 flex flex-col md:flex-row items-center justify-between gap-6">
                        <div className="space-y-2 text-center md:text-left">
                            <h3 className="font-display text-headline-md">Enjoying these insights?</h3>
                            <p className="font-sans text-body-md text-surface-variant">Get the deep-dives delivered to your inbox every Thursday.</p>
                        </div>
                        <Link 
                            href="/#subscribe" 
                            className="bg-primary-container text-on-primary-container font-sans text-label-bold px-8 py-4 rounded-full hover:bg-primary-fixed transition-all active:scale-95 whitespace-nowrap shadow-lg glow-yellow"
                        >
                            Subscribe to Newsletter
                        </Link>
                    </div>
                </article>

                {/* Sidebar */}
                <aside className="lg:col-span-4 space-y-8">
                    <div className="sticky top-28 space-y-8">
                        
                        {/* Reference Feed */}
                        <div className="space-y-6">
                            <div className="flex items-center justify-between">
                                <h3 className="font-sans text-label-bold uppercase text-on-surface-variant">
                                    Reference Feed
                                </h3>
                                <span className="bg-surface-container-high px-2 py-0.5 rounded text-caption font-caption font-semibold text-on-surface-variant animate-pulse">
                                    LIVE UPDATES
                                </span>
                            </div>

                            {sources.length > 0 ? (
                                <div className="space-y-4">
                                    {sources.map((source, index) => {
                                        const type = getSourceType(source.url);
                                        return (
                                            <a
                                                key={index}
                                                href={source.url}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className="block bg-surface-container-low border border-outline-variant rounded-xl p-5 glow-yellow-hover hover:border-primary-container transition-all group"
                                            >
                                                <div className="flex items-center gap-3 mb-3">
                                                    {type === 'twitter' && (
                                                        <>
                                                            <Twitter className="h-5 w-5 text-[#1DA1F2]" />
                                                            <span className="font-sans text-label-bold text-on-surface">Twitter / X</span>
                                                        </>
                                                    )}
                                                    {type === 'reddit' && (
                                                        <>
                                                            <MessageSquare className="h-5 w-5 text-[#FF4500]" />
                                                            <span className="font-sans text-label-bold text-on-surface">Reddit Community</span>
                                                        </>
                                                    )}
                                                    {type === 'news' && (
                                                        <>
                                                            <Globe className="h-5 w-5 text-primary" />
                                                            <span className="font-sans text-label-bold text-on-surface">News Analysis</span>
                                                        </>
                                                    )}
                                                    <span className="ml-auto text-caption font-caption text-on-surface-variant flex items-center gap-0.5">
                                                        <Clock className="h-3 w-3" />
                                                        Verified
                                                    </span>
                                                </div>
                                                <p className="font-sans text-caption text-on-surface-variant mb-3">
                                                    {source.snippet || source.title}
                                                </p>
                                                <div className="flex items-center gap-2 text-primary font-sans text-label-bold text-xs">
                                                    <span>
                                                        {type === 'twitter' ? 'View Thread' : type === 'reddit' ? 'Join Discussion' : 'Read Full Report'}
                                                    </span>
                                                    <ArrowUpRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                                                </div>
                                            </a>
                                        );
                                    })}
                                </div>
                            ) : (
                                <div className="bg-surface-container-low border border-outline-variant rounded-xl p-6 text-center">
                                    <p className="font-sans text-caption text-on-surface-variant">
                                        No references attached to this edition.
                                    </p>
                                </div>
                            )}
                        </div>

                        {/* Trending Topics */}
                        <div className="bg-surface-container rounded-2xl p-6 space-y-4">
                            <h3 className="font-sans text-label-bold text-on-surface">Trending in AI</h3>
                            <div className="flex flex-wrap gap-2">
                                <span className="bg-white dark:bg-black border border-outline-variant px-3 py-1 rounded-full text-caption font-semibold hover:border-primary cursor-pointer transition-colors text-on-surface">
                                    #AgentSwarm
                                </span>
                                <span className="bg-white dark:bg-black border border-outline-variant px-3 py-1 rounded-full text-caption font-semibold hover:border-primary cursor-pointer transition-colors text-on-surface">
                                    #TokenEconomics
                                </span>
                                <span className="bg-white dark:bg-black border border-outline-variant px-3 py-1 rounded-full text-caption font-semibold hover:border-primary cursor-pointer transition-colors text-on-surface">
                                    #RAG2.0
                                </span>
                                <span className="bg-white dark:bg-black border border-outline-variant px-3 py-1 rounded-full text-caption font-semibold hover:border-primary cursor-pointer transition-colors text-on-surface">
                                    #GenerativeAI
                                </span>
                            </div>
                        </div>

                        {/* Newsletter Stats Summary Box */}
                        <div className="left-accent-bar bg-surface-container-high p-6 rounded-xl border border-outline-variant">
                            <h4 className="font-sans text-caption text-on-surface-variant uppercase mb-1">
                                Edition Impact
                            </h4>
                            <div className={`font-display text-headline-md ${sentimentColor}`}>
                                {sentimentScore}
                            </div>
                            <p className="font-sans text-caption text-on-surface-variant flex items-center gap-1 mt-1">
                                <TrendingUp className="h-3 w-3" />
                                Reader Sentiment ({newsletter.sentiment})
                            </p>
                        </div>
                    </div>
                </aside>
            </div>
        </main>
    );
}
