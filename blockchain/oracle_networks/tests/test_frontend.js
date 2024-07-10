import React from 'eact';
import { render, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

describe('App', () => {
    it('renders nodes list', () => {
        const { getByText } = render(<App />);
        expect(getByText('Oracle Network Interface')).toBeInTheDocument();
    });

    it('renders node balance', () => {
        const { getByText } = render(<App />);
        expect(getByText('Node Balance: 0')).toBeInTheDocument();
    });

    it('sends transaction', async () => {
        const { getByText, getByLabelText } = render(<App />);
        const fromInput = getByLabelText('From');
        const toInput = getByLabelText('To');
        const amountInput = getByLabelText('Amount');
        const submitButton = getByText('Send Transaction');

        fireEvent.change(fromInput, { target: { value: '0x...UserAddress...' } });
        fireEvent.change(toInput, { target: { value: '0x...NodeAddress...' } });
        fireEvent.change(amountInput, { target: { value: 10 } });

        await waitFor(() => fireEvent.click(submitButton));

        expect(submitButton).toBeDisabled();
    });
});
