'use client';

import { useEffect, useState } from 'react';
import api from '@/utils/api';
import { Search, Loader2, Calendar, ShieldCheck, HelpCircle } from 'lucide-react';

interface Subscriber {
    id: number;
    email: string;
    subscribed_at: string;
    is_active: boolean;
}

interface SubscribersListProps {
    onListUpdated?: () => void;
}

export default function SubscribersList({ onListUpdated }: SubscribersListProps) {
    const [subscribers, setSubscribers] = useState<Subscriber[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5;

    useEffect(() => {
        fetchSubscribers();
    }, []);

    const fetchSubscribers = async () => {
        try {
            setLoading(true);
            const response = await api.get('/subscribers/');
            setSubscribers(response.data);
        } catch (error) {
            console.error('Failed to fetch subscribers', error);
        } finally {
            setLoading(false);
        }
    };

    // Filter list
    const filteredSubscribers = subscribers.filter(sub => 
        sub.email.toLowerCase().includes(searchTerm.toLowerCase())
    );

    // Pagination
    const totalItems = filteredSubscribers.length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);
    const displayedItems = filteredSubscribers.slice(
        (currentPage - 1) * itemsPerPage,
        currentPage * itemsPerPage
    );

    // Get email initials
    const getInitials = (email: string) => {
        if (!email) return 'AI';
        const parts = email.split('@');
        return parts[0].slice(0, 2).toUpperCase();
    };

    // Determine mock source based on email host (for visual appeal matching Stitch)
    const getMockSource = (email: string) => {
        const lower = email.toLowerCase();
        if (lower.includes('gmail') || lower.includes('google')) return 'Google';
        if (lower.includes('linkedin')) return 'LinkedIn';
        if (lower.includes('twitter') || lower.includes('x.com')) return 'Twitter';
        if (lower.includes('tech') || lower.includes('hub')) return 'TechHub';
        return 'Direct';
    };

    return (
        <div className="bg-surface-container-low border border-outline-variant rounded-2xl overflow-hidden flex flex-col h-full text-on-background">
            {/* Header section */}
            <div className="p-6 border-b border-outline-variant flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                <div>
                    <h3 className="font-display text-2xl font-bold">Subscriber List</h3>
                    <p className="font-sans text-caption text-on-surface-variant mt-1 font-semibold">
                        Total Registered: {subscribers.length}
                    </p>
                </div>
                
                {/* Search Bar */}
                <div className="relative w-full sm:w-64">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant h-4 w-4" />
                    <input
                        type="text"
                        placeholder="Filter by email..."
                        value={searchTerm}
                        onChange={(e) => {
                            setSearchTerm(e.target.value);
                            setCurrentPage(1);
                        }}
                        className="w-full bg-surface-container-lowest border border-outline-variant rounded-full text-caption py-2 pl-9 pr-4 focus:outline-none focus:border-primary transition-all font-medium placeholder:text-on-surface-variant/40"
                    />
                </div>
            </div>

            {/* List Table */}
            <div className="flex-grow overflow-x-auto no-scrollbar">
                {loading ? (
                    <div className="flex justify-center items-center py-20">
                        <Loader2 className="animate-spin h-8 w-8 text-primary" />
                    </div>
                ) : (
                    <table className="w-full text-left">
                        <thead className="bg-surface-container-high border-b border-outline-variant font-sans text-label-bold font-bold text-on-surface-variant">
                            <tr>
                                <th className="px-6 py-4">User Details</th>
                                <th className="px-6 py-4">Join Date</th>
                                <th className="px-6 py-4">Channel</th>
                                <th className="px-6 py-4 text-center">Status</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-outline-variant">
                            {displayedItems.map((sub) => {
                                const initials = getInitials(sub.email);
                                const source = getMockSource(sub.email);
                                const joinDate = new Date(sub.subscribed_at).toLocaleDateString('en-US', {
                                    year: 'numeric',
                                    month: 'short',
                                    day: 'numeric'
                                });

                                return (
                                    <tr key={sub.id} className="hover:bg-surface-container transition-colors group">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center font-sans text-label-bold font-bold text-xs shadow-sm">
                                                    {initials}
                                                </div>
                                                <div className="truncate max-w-[200px]">
                                                    <p className="font-sans text-label-bold font-bold text-on-background leading-none mb-1">
                                                        {sub.email.split('@')[0]}
                                                    </p>
                                                    <p className="font-sans text-caption text-on-surface-variant font-medium">
                                                        {sub.email}
                                                    </p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-6 py-4 font-sans text-body-md font-semibold text-on-surface-variant">
                                            {joinDate}
                                        </td>
                                        <td className="px-6 py-4">
                                            <span className={`px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider rounded-full ${
                                                source === 'LinkedIn' ? 'bg-[#0077B5]/10 text-[#0077B5]' :
                                                source === 'Twitter' ? 'bg-[#1DA1F2]/10 text-[#1DA1F2]' :
                                                source === 'Google' ? 'bg-[#DB4437]/10 text-[#DB4437]' :
                                                source === 'TechHub' ? 'bg-[#705d00]/10 text-[#705d00]' :
                                                'bg-surface-container-highest text-on-surface-variant border border-outline-variant'
                                            }`}>
                                                {source}
                                            </span>
                                        </td>
                                        <td className="px-6 py-4 text-center">
                                            <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold ${
                                                sub.is_active 
                                                    ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' 
                                                    : 'bg-rose-50 text-rose-700 border border-rose-200'
                                            }`}>
                                                <span className={`w-1.5 h-1.5 rounded-full ${sub.is_active ? 'bg-emerald-500' : 'bg-rose-500'}`}></span>
                                                {sub.is_active ? 'Active' : 'Inactive'}
                                            </span>
                                        </td>
                                    </tr>
                                );
                            })}

                            {displayedItems.length === 0 && (
                                <tr>
                                    <td colSpan={4} className="text-center py-12 text-on-surface-variant font-medium">
                                        No subscribers found.
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                )}
            </div>

            {/* Pagination / Table Footer */}
            {!loading && totalItems > 0 && (
                <div className="mt-auto p-4 flex justify-between items-center border-t border-outline-variant bg-surface-container-low">
                    <p className="font-sans text-caption font-semibold text-on-surface-variant">
                        Showing {Math.min(totalItems, (currentPage - 1) * itemsPerPage + 1)} to {Math.min(totalItems, currentPage * itemsPerPage)} of {totalItems} subscribers
                    </p>
                    
                    <div className="flex gap-2">
                        <button
                            onClick={() => setCurrentPage(prev => Math.max(1, prev - 1))}
                            disabled={currentPage === 1}
                            className="p-2 hover:bg-surface-container-high rounded-lg transition-colors text-on-surface-variant disabled:opacity-40"
                        >
                            ← Previous
                        </button>
                        <button
                            onClick={() => setCurrentPage(prev => Math.min(totalPages, prev + 1))}
                            disabled={currentPage === totalPages || totalPages === 0}
                            className="p-2 hover:bg-surface-container-high rounded-lg transition-colors text-on-surface-variant disabled:opacity-40"
                        >
                            Next →
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}
