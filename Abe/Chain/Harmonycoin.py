# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X13PosChain import X13PosChain

class Harmonycoin(X13PosChain):
    def __init__(chain, **kwargs):
        chain.name = 'Harmonycoin'
        chain.code3 = 'HMY'
        chain.address_version = '\x19'
        chain.magic = '\x70\x35\x22\x05'
        X13PosChain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'harmonycoin.conf'
