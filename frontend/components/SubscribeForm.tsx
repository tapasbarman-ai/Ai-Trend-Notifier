'use client';

import { useState } from 'react';
import api from '@/utils/api';
import { Loader2 } from 'lucide-react';

export default function SubscribeForm() {
    const [email, setEmail] = useState('');
    const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setStatus('loading');
        try {
            await api.post('/subscribers/', { email });
            setStatus('success');
            setMessage('Thanks for subscribing! You are on the list.');
            setEmail('');
        } catch (error: any) {
            setStatus('error');
            setMessage(error.response?.data?.detail || 'Something went wrong. Please try again.');
        }
    };

    return (
        <div className="w-full max-w-md mx-auto" id="subscribe">
            <form onSubmit={handleSubmit} className="flex flex-col gap-4 sm:flex-row">
                <input
                    type="email"
                    placeholder="Enter your email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    className="flex-1 px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-black focus:outline-none focus:ring-2 focus:ring-accent"
                    disabled={status === 'loading' || status === 'success'}
                />
                <button
                    type="submit"
                    disabled={status === 'loading' || status === 'success'}
                    className="px-6 py-3 bg-primary text-white dark:bg-white dark:text-black rounded-lg font-medium hover:opacity-90 transition-opacity disabled:opacity-50 flex items-center justify-center"
                >
                    {status === 'loading' ? <Loader2 className="animate-spin h-5 w-5" /> : 'Subscribe'}
                </button>
            </form>
            {message && (
                <p className={`mt-4 text-sm text-center ${status === 'success' ? 'text-green-600' : 'text-red-600'}`}>
                    {message}
                </p>
            )}
        </div>
    );
}
