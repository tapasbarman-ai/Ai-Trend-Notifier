'use client';

import { useState } from 'react';
import api from '@/utils/api';
import { Mail, Rocket, Sparkles, AlertCircle, CheckCircle2 } from 'lucide-react';

interface CreateNewsletterFormProps {
    onNewsletterCreated?: () => void;
}

export default function CreateNewsletterForm({ onNewsletterCreated }: CreateNewsletterFormProps) {
    const [formData, setFormData] = useState({
        title: '',
        summary: '',
        content: '',
        sentiment: 'Neutral'
    });
    const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setStatus('loading');
        try {
            await api.post('/newsletters/', formData);
            setStatus('success');
            setFormData({ title: '', summary: '', content: '', sentiment: 'Neutral' });
            if (onNewsletterCreated) {
                onNewsletterCreated();
            }
            setTimeout(() => setStatus('idle'), 3000);
        } catch (error) {
            setStatus('error');
        }
    };

    return (
        <div className="bg-surface-container-lowest border-2 border-primary-container p-8 rounded-2xl shadow-[0_10px_30px_rgba(255,215,0,0.1)] h-fit text-on-background">
            <div className="flex items-center gap-3 mb-6">
                <Mail className="text-primary h-8 w-8" />
                <h3 className="font-display text-2xl font-bold uppercase tracking-tight">Create Newsletter</h3>
            </div>
            
            <form onSubmit={handleSubmit} className="space-y-6">
                {/* Title Input */}
                <div className="group">
                    <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-colors">
                        Subject Line
                    </label>
                    <input
                        type="text"
                        value={formData.title}
                        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                        className="w-full bg-transparent border-b border-outline outline-none py-3 font-sans text-body-md transition-all focus:border-primary focus:border-b-2 text-on-surface placeholder:text-on-surface-variant/40"
                        placeholder="e.g. Weekly AI Pulse..."
                        required
                        disabled={status === 'loading'}
                    />
                </div>

                {/* Sentiment Dropdown */}
                <div className="group">
                    <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-colors">
                        Market Sentiment
                    </label>
                    <select
                        value={formData.sentiment}
                        onChange={(e) => setFormData({ ...formData, sentiment: e.target.value })}
                        className="w-full bg-transparent border-b border-outline outline-none py-3 font-sans text-body-md transition-all focus:border-primary focus:border-b-2 text-on-surface select-custom cursor-pointer"
                        disabled={status === 'loading'}
                    >
                        <option value="Positive">Positive</option>
                        <option value="Neutral">Neutral</option>
                        <option value="Negative">Negative</option>
                    </select>
                </div>

                {/* Summary Textarea */}
                <div className="group">
                    <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-colors">
                        Executive Summary
                    </label>
                    <textarea
                        value={formData.summary}
                        onChange={(e) => setFormData({ ...formData, summary: e.target.value })}
                        className="w-full bg-transparent border-b border-outline outline-none py-3 font-sans text-body-md transition-all focus:border-primary focus:border-b-2 text-on-surface resize-none h-20 placeholder:text-on-surface-variant/40"
                        placeholder="Brief executive summary of the latest AI trends..."
                        required
                        disabled={status === 'loading'}
                    />
                </div>

                {/* Content Textarea */}
                <div className="group">
                    <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-colors">
                        Edition Content
                    </label>
                    <textarea
                        value={formData.content}
                        onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                        className="w-full bg-transparent border-b border-outline outline-none py-3 font-sans text-body-md transition-all focus:border-primary focus:border-b-2 text-on-surface resize-none h-40 placeholder:text-on-surface-variant/40"
                        placeholder="Full analytical context. (To append sources, use 'Enriched Data:' followed by a JSON list)"
                        required
                        disabled={status === 'loading'}
                    />
                </div>

                {/* Status messages */}
                {status === 'success' && (
                    <div className="flex items-center gap-2 text-emerald-600 bg-emerald-50 border border-emerald-200 rounded-xl p-3 text-sm font-semibold">
                        <CheckCircle2 className="h-4 w-4" />
                        <span>Newsletter created and published successfully!</span>
                    </div>
                )}
                {status === 'error' && (
                    <div className="flex items-center gap-2 text-rose-600 bg-rose-50 border border-rose-200 rounded-xl p-3 text-sm font-semibold">
                        <AlertCircle className="h-4 w-4" />
                        <span>Failed to send newsletter campaign. Please retry.</span>
                    </div>
                )}

                {/* Launch Campaign Button */}
                <button
                    type="submit"
                    disabled={status === 'loading'}
                    className="w-full py-4 bg-primary text-on-primary rounded-xl font-sans text-label-bold font-bold border-2 border-primary hover:bg-transparent hover:text-primary transition-all active:scale-95 flex items-center justify-center gap-2 disabled:opacity-50"
                >
                    {status === 'loading' ? (
                        <>
                            <span>Publishing...</span>
                            <Rocket className="h-5 w-5 animate-pulse" />
                        </>
                    ) : (
                        <>
                            <span>Launch Campaign</span>
                            <Rocket className="h-5 w-5" />
                        </>
                    )}
                </button>
            </form>
        </div>
    );
}
