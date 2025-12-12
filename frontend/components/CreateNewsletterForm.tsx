'use client';

import { useState } from 'react';
import api from '@/utils/api';

export default function CreateNewsletterForm() {
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
            setTimeout(() => setStatus('idle'), 3000);
        } catch (error) {
            setStatus('error');
        }
    };

    return (
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
            <h2 className="text-lg font-bold mb-4">Create Newsletter</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-sm font-medium mb-1">Title</label>
                    <input
                        type="text"
                        value={formData.title}
                        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-black"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Sentiment</label>
                    <select
                        value={formData.sentiment}
                        onChange={(e) => setFormData({ ...formData, sentiment: e.target.value })}
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-black"
                    >
                        <option value="Positive">Positive</option>
                        <option value="Neutral">Neutral</option>
                        <option value="Negative">Negative</option>
                    </select>
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Summary</label>
                    <textarea
                        value={formData.summary}
                        onChange={(e) => setFormData({ ...formData, summary: e.target.value })}
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-black h-20"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Content</label>
                    <textarea
                        value={formData.content}
                        onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-black h-40"
                        required
                    />
                </div>
                <button
                    type="submit"
                    disabled={status === 'loading'}
                    className="px-6 py-2 bg-primary text-white dark:bg-white dark:text-black rounded-lg font-medium hover:opacity-90 disabled:opacity-50"
                >
                    {status === 'loading' ? 'Sending...' : 'Send Newsletter'}
                </button>
                {status === 'success' && <p className="text-green-600 text-sm">Newsletter sent successfully!</p>}
                {status === 'error' && <p className="text-red-600 text-sm">Failed to send newsletter.</p>}
            </form>
        </div>
    );
}
