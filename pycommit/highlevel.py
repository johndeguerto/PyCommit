from pycommit import lowlevel, entities
import sys

class AmbiguousValue(Exception):
    pass

class DBInterface(object):
    def __init__(self, crm_path):
        self.crm_path = crm_path
        self.crm_db = None
        
        self.calls_per_handle = 1000
        self.db_call_cnt = 0

    # This is a hack to free up memory from the low level DB interface
    def db_operation(self):
        if self.db_call_cnt > self.calls_per_handle or not self.crm_db:
            self.crm_db = lowlevel.DBInterface(CRMPath=self.crm_path)
            self.db_call_cnt = 0
        else:
            self.db_call_cnt += 1

    def get_recids(self, entity, search_criteria):
        self.db_operation()
        
        query = 'FROM {} SELECT * WHERE {} = "{}" '

        search_keys = list(search_criteria.keys())

        key = search_keys.pop()
        query = query.format(entity, key, search_criteria.pop(key))

        for _, _ in search_criteria.items():
            key = search_keys.pop()
            query += 'AND {} = "{}" '.format(key, search_criteria[key])

        req = lowlevel.RecIDRequest(query.format(entity=entity, **search_criteria),
                                    maxRecordCnt = 32768)

        try:
            rec_ids = self.crm_db.query_recids(req)
        except lowlevel.QueryError as e:
            print(e)
            return

        return rec_ids

    def find_record(self, entity, value, fields):
        self.db_operation()
        
        for f in fields:
            req = lowlevel.RecIDRequest(
                query='FROM {} SELECT * WHERE {} = "{}"'.format(
                    entity, f, value))
            
            try:
                rec_ids = self.crm_db.query_recids(req)
            except lowlevel.QueryError as e:
                print(e)
                return
            
            recid = None
            if rec_ids is not None: recid = rec_ids[0]
            return recid

    def get_field(self, recid, field):
        self.db_operation()
        
        req = lowlevel.RecordDataRequest(
            query = "FROM {} SELECT ({})".format(
                recid, field))

        try:
            data = self.crm_db.get_rec_data_by_recid(req)
        except lowlevel.QueryError as e:
            print(e)
            return ''

        if data is None: return
        ret = data[field]
        return ret

    def update_record_from_dict(self, entity, data):
        self.db_operation()
        
        if (entity is None) or (data is None):
            return
        
        data_str, map_str = '', "'\n,\n"
        
        for key, value in data.items():
            data_str += "'{}',".format(value)
            map_str += "{}\n".format(key)

        rec = lowlevel.DBRecord(entity, data_str, map_str)

        try:
            self.crm_db.update_rec(rec)
        except lowlevel.QueryError as e:
            print(e)
            return

        recid = rec.getRecID()
        return recid

    def update_record(self, entity, **kwargs):
        return update_record_from_dict(entity, kwargs)