import streamlit as st
from ipwhois import IPWhois
from ipwhois.exceptions import IPDefinedError
import pandas as pd

def get_ip_info(ip_address):
    try:
        obj = IPWhois(ip_address)
        results = obj.lookup_rdap()
        return results
    except IPDefinedError:
        return {'error': 'Invalid IP address'}
    except Exception as e:
        return {'error': str(e)}

st.title('IP Address Lookup')
st.write('Enter an IP address to get detailed information.')

ip_address = st.text_input('IP Address', '')

if ip_address:
    ip_info = get_ip_info(ip_address)
    if 'error' in ip_info:
        st.write(ip_info['error'])
    else:
        # Display the results as a column-wise table
        st.write('### IP Information')
        flattened_data = pd.json_normalize(ip_info).transpose()
        st.dataframe(flattened_data)
        st.write('### Raw JSON Data')
        st.json(ip_info)
