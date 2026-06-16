'use client';

import { useEffect, useState } from 'react';
import api from '@/utils/api';
import NewsletterCard from '@/components/NewsletterCard';
import { Loader2, Search } from 'lucide-react';

interface Newsletter {
    id: number;
    title: string;
    summary: string;
    content: string;
    sentiment: string;
    published_at: string;
}

const TAG_OPTIONS = [
    'All Editions',
    'Generative AI',
    'Robotics',
    'Ethics',
    'Hardware'
];

export default function NewslettersPage() {
    const [newsletters, setNewsletters] = useState<Newsletter[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedTag, setSelectedTag] = useState('All Editions');
    const [visibleCount, setVisibleCount] = useState(6);

    useEffect(() => {
        const fetchNewsletters = async () => {
            try {
                const response = await api.get('/newsletters/');
                setNewsletters(response.data);
            } catch (error) {
                console.error('Failed to fetch newsletters', error);
            } finally {
                setLoading(false);
            }
        };
        fetchNewsletters();
    }, []);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-[50vh]">
                <Loader2 className="animate-spin h-8 w-8 text-primary" />
            </div>
        );
    }

    const filtered = newsletters.filter((newsletter) => {
        const matchesSearch = 
            newsletter.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
            newsletter.summary.toLowerCase().includes(searchTerm.toLowerCase());
        
        if (!matchesSearch) return false;
        
        if (selectedTag === 'All Editions') return true;
        
        const textToSearch = `${newsletter.title} ${newsletter.summary} ${newsletter.content}`.toLowerCase();
        
        switch (selectedTag) {
            case 'Generative AI':
                return textToSearch.includes('generative') || textToSearch.includes('llm') || textToSearch.includes('model') || textToSearch.includes('neural') || textToSearch.includes('gpt') || textToSearch.includes('claude') || textToSearch.includes('swarm') || textToSearch.includes('agent');
            case 'Robotics':
                return textToSearch.includes('robot') || textToSearch.includes('haptic') || textToSearch.includes('tactile') || textToSearch.includes('machinery');
            case 'Ethics':
                return textToSearch.includes('ethic') || textToSearch.includes('privacy') || textToSearch.includes('bias') || textToSearch.includes('transparency') || textToSearch.includes('sovereignty');
            case 'Hardware':
                return textToSearch.includes('hardware') || textToSearch.includes('chip') || textToSearch.includes('semiconductor') || textToSearch.includes('quantum') || textToSearch.includes('edge') || textToSearch.includes('compute');
            default:
                return true;
        }
    });

    const displayedNewsletters = filtered.slice(0, visibleCount);
    const hasMore = filtered.length > visibleCount;

    return (
        <main className="max-w-container-max-width mx-auto px-margin-mobile md:px-margin-desktop py-12 text-on-background">
            {/* Hero Section & Filters */}
            <section className="mb-16">
                <div className="flex flex-col md:flex-row md:items-end justify-between gap-8">
                    <div>
                        <div className="flex items-center gap-2 mb-2">
                            <span className="h-2 w-2 rounded-full bg-primary animate-pulse"></span>
                            <span className="text-caption font-caption text-primary uppercase">
                                Archive Feed ({filtered.length} Editions)
                            </span>
                        </div>
                        <h1 className="font-display text-display-xl text-on-background mb-4">
                            Edition Archive
                        </h1>
                        <p className="font-sans text-body-lg text-on-surface-variant max-w-2xl">
                            Explore our curated collection of deep dives into generative efficiency, neural architectures, and the future of human-AI collaboration.
                        </p>
                    </div>
                    {/* Search & Filter Bar */}
                    <div className="w-full md:w-auto">
                        <div className="relative group">
                            <input
                                value={searchTerm}
                                onChange={(e) => {
                                    setSearchTerm(e.target.value);
                                    setVisibleCount(6);
                                }}
                                className="w-full md:w-80 bg-surface-container-low border-0 border-b-2 border-outline-variant focus:border-primary focus:ring-0 transition-all font-sans text-body-md py-3 pl-4 pr-12 text-on-surface placeholder:text-on-surface-variant/50 outline-none rounded-t-lg"
                                placeholder="Search editions..."
                                type="text"
                            />
                            <Search className="absolute right-4 top-1/2 -translate-y-1/2 text-primary h-5 w-5" />
                        </div>
                    </div>
                </div>

                {/* Filter Chips */}
                <div className="flex flex-wrap gap-3 mt-8">
                    {TAG_OPTIONS.map((tag) => {
                        const isActive = selectedTag === tag;
                        return (
                            <button
                                key={tag}
                                onClick={() => {
                                    setSelectedTag(tag);
                                    setVisibleCount(6);
                                }}
                                className={`px-4 py-2 rounded-full font-sans text-label-bold transition-all ${
                                    isActive
                                        ? 'bg-primary-container text-on-primary-container glow-accent'
                                        : 'bg-surface-container-high text-on-surface-variant hover:bg-surface-container-highest'
                                }`}
                            >
                                {tag}
                            </button>
                        );
                    })}
                </div>
            </section>

            {/* Latest Editions Heading */}
            <div className="flex items-center gap-4 mb-8">
                <h2 className="font-display text-headline-lg text-on-background">Latest Editions</h2>
                <div className="h-[1px] flex-grow bg-outline-variant"></div>
            </div>

            {/* Edition Grid */}
            <div className="grid gap-gutter md:grid-cols-2 lg:grid-cols-3">
                {displayedNewsletters.map((newsletter) => (
                    <NewsletterCard
                        key={newsletter.id}
                        id={newsletter.id}
                        title={newsletter.title}
                        summary={newsletter.summary}
                        sentiment={newsletter.sentiment}
                        published_at={newsletter.published_at}
                    />
                ))}
            </div>

            {filtered.length === 0 && (
                <div className="bg-surface-container-low border border-outline-variant rounded-2xl p-12 text-center max-w-md mx-auto mt-12">
                    <p className="text-on-surface-variant font-body-md">No editions found matching your filters.</p>
                </div>
            )}

            {/* Load More Section */}
            {hasMore && (
                <div className="flex justify-center mt-16">
                    <button
                        onClick={() => setVisibleCount((prev) => prev + 6)}
                        className="group flex items-center gap-3 px-8 py-4 bg-surface-container-low border-2 border-primary text-primary font-sans text-label-bold rounded-xl hover:bg-primary-container hover:text-on-primary-container transition-all glow-accent active:scale-95"
                    >
                        Load Previous Editions
                        <span className="transition-transform duration-300 group-hover:translate-y-1">↓</span>
                    </button>
                </div>
            )}
        </main>
    );
}
