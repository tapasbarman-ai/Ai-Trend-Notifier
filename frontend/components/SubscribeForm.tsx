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
        <div className="w-full max-w-md mx-auto">
            <form onSubmit={handleSubmit} className="flex flex-col gap-3 sm:flex-row p-1.5 rounded-xl bg-white/5 border border-white/10 backdrop-blur-md">
                <input
                    type="email"
                    placeholder="Enter your email address..."
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    className="flex-1 px-4 py-3 rounded-lg bg-transparent text-white placeholder-gray-400 focus:outline-none text-sm transition-all"
                    disabled={status === 'loading' || status === 'success'}
                />
                <button
                    type="submit"
                    disabled={status === 'loading' || status === 'success'}
                    className="px-6 py-3 bg-gradient-to-r from-primary to-accent text-white rounded-lg text-sm font-semibold hover:brightness-110 active:scale-95 transition-all shadow-md shadow-primary/10 disabled:opacity-50 flex items-center justify-center min-w-[110px]"
                >
                    {status === 'loading' ? <Loader2 className="animate-spin h-4 w-4" /> : 'Subscribe'}
                </button>
            </form>
            {message && (
                <p className={`mt-3 text-xs text-center font-medium ${status === 'success' ? 'text-green-400' : 'text-rose-400'}`}>
                    {message}
                </p>
            )}
        </div>

    );
}
