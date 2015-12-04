class CRMEntity(object):
    types = {
        "Account": 10,
        "Accounts": 10,
        "Opportunitity": 20,
        "Opportunities": 20,
        "Document": 30,
        "Documents": 30,
        "Charge": 40,
        "Charges": 40,
        "Event": 50,
        "Events": 50,
        "HistoryNote": 60,
        "HistoryNotes": 60,
        "Ticket": 70,
        "Tickets": 70,
        "Item": 80,
        "Items": 80,
        "Asset": 90,
        "Assets": 90,
        "KBArticle": 100,
        "KBArticles": 100
    }

    def __init__(self, recid=None, crm_proxy=None, auto_populate=True):
        self._recid = recid
        self._crm_proxy = crm_proxy

        self.db_data = {}
        self.entity_type = None

        if self._crm_proxy is None:
            raise Exception

        if self._recid is not None and auto_populate is True:
            self._populate()

    def get_recid(self):
        return self._recid

    def get_field(self, field):
        return self.db_data[field]

    def set_field(self, field, value):
        self.db_data[field] = value

    def create(self):
        if self._recid is not None:
            return

        self._db_sync()

    def update(self):
        if self._recid is None:
            return

        self._db_sync()

    def _db_sync(self):
        self._crm_proxy.update_record(self._recid, self.db_data)

    def _populate(self):
        field_names = []
        for _, field_name in self.db_fields.items():
            value = self._crm_proxy.get_field(self._recid, field_name)
            if value: self.db_data[field_name] = value

class Account(CRMEntity):
    db_fields = {
        "AccountRecID": "FLDCRDRECID",
        "AccountMgr": "FLDCRDASSIGNCARDID",
        "SubContStatus": "FLDCRDSUBCONTSTATUS",
        "CompanyName": "FLDCRDCOMPANY",
        "Contact": "FLDCRDCONTACT",
        "Username": "FLDWRKUSERNAME",
        "Assistant": "FLDCRDASSISTANT",
        "Contract": "FLDCRDBCRECID",
        "AccountNumber": "FLDCRDCARDID2",
        "ID": "FLDCRDCARDID3",
        "PopupMessage": "FLDCRDCARDMESSAGE",
        "AddressLn1": "FLDCRDADDRESS1",
        "AddressLn2": "FLDCRDADDRESS2",
        "AddressLn3": "FLDCRDADDRESS3",
        "AddressCity": "FLDCRDCITY",
        "AddressState": "FLDCRDSTATE",
        "AddressCountry": "FLDCRDCOUNTRY",
        "AddressZip": "FLDCRDZIP",
        "CreationDate": "FLDCRDCREATEDATE",
        "CreatedByUser": "FLDCRDCREATEUSERID",
        "Dear": "FLDCRDDEAR",
        "Department": "FLDCRDDEPARTMENT",
        "DocStorDir": "FLDCRDDOCSFOLDER",
        "Email1": "FLDCRDEMAIL1",
        "Email2": "FLDCRDEMAIL1",
        "AccountType": "FLDCRDENTITYKIND",
        "FaxNumber": "FLDCRDFAX1",
        "FaxExt": "FLDCRDFAXDESC1",
        "FileAs": "FLDCRDFULLNAME",
        "Type": "FLDCRDKIND",
        "LastName": "FLDCRDLASTNAME",
        "Notes": "FLDCRDNOTES",
        "Field": "FLDCRDPERSONID",
        "Phone1": "FLDCRDPHONE1",
        "Phone2": "FLDCRDPHONE2",
        "Phone3": "FLDCRDPHONE3",
        "Phone4": "FLDCRDPHONE4",
        "PhoneExt1": "FLDCRDPHNDESC1",
        "PhoneExt2": "FLDCRDPHNDESC2",
        "PhoneExt3": "FLDCRDPHNDESC3",
        "PhoneExt4": "FLDCRDPHNDESC4",
        "Region": "FLDCRDREGIONCODE",
        "PopMessIndc": "FLDCRDSHOWMESSAGE",
        "SubContactCode": "FLDCRDSUBCODE",
        "Salutation": "FLDCRDSUFFIX",
        "Tax1": "FLDCRDTAXCODE1",
        "Tax2": "FLDCRDTAXCODE2",
        "Title": "FLDCRDTITLE",
        "LastUpdtBy": "FLDCRDUPDATEUSERID",
        "WebAddr1": "FLDCRDURL1",
        "WebAddr2": "FLDCRDURL2",
        "Status": "FLDCRDUSER1",
        "Field1": "FLDCRDUSER2",
        "Field2": "FLDCRDUSER3",
        "Field3": "FLDCRDUSER4",
        "Field4": "FLDCRDUSER5"
    }

    def __init__(self, recid=None, crm_proxy=None):
        super().__init__(recid, crm_proxy)

class Asset(CRMEntity):
    db_fields = {
        "Code": "FLDASTASSETCODE",
        "Type": "FLDASTASSETTYPE",  # Required
        "Name": "FLDASTNAME",
        "Status": "FLDASTSTATUS",   # Required
        "RecordID": "FLDASTRECID",
        "SerialNo": "FLDASTSERIALNO",
        "AccountRecID": "FLDASTACCRECID",
        "Contact": "FLDASTCONTACTRECID",
        "CreatedByUser": "FLDASTCREATEUSER",
        "PurchaseDate": "FLDASTCUSTPURDATE",
        "PurchasedFromUs": "FLDASTCUSTPURFROMUS",
        "PurchaseInvoiceNo": "FLDASTCUSTPUROURINV",
        "CustomerPO": "FLDASTCUSTPURPO",
        "PurchasePrice": "FLDASTCUSTPURPRICE",
        "DeliveredDate": "FLDASTDELIVEDATE",
        "Description": "FLDASTDESC",
        "InstalledBy": "FLDASTINSTALBY",
        "InstalledDate": "FLDASTINSTALDATE",
        "LicenseCodes": "FLDASTLICENSECODE",
        "LicenseKeys": "FLDASTLICENSEKEYS",
        "LicenseNotes": "FLDASTLICENSENOTES",
        "Location": "FLDASTLOCATION",
        "Manufacturer": "FLDASTMANUFACTURER",
        "MnfSerialNo": "FLDASTMNFSERIALNO",
        "Model": "FLDASTMODEL",
        "Notes": "FLDASTNOTES",
        "Quantity": "FLDASTQUANTITY",
        "LastUpdateBy": "FLDASTUPDATEUSER",
        "Field1": "FLDASTUSER1",
        "Field2": "FLDASTUSER2",
        "Field3": "FLDASTUSER3",
        "Field4": "FLDASTUSER4",
        "Field5": "FLDASTUSER5",
        "Date1": "FLDASTUSERDATE1",
        "Number1": "FLDASTUSERNUMBER1",
        "VendorPurchDate": "FLDASTVENDORDATEPURC",
        "VendorInvoiceNo": "FLDASTVENDORINVNO",
        "VendorPO": "FLDASTVENDOROURPO",
        "VendorPrice": "FLDASTVENDORPRICE",
        "Vendor": "FLDASTVENDORRECID",
        "VendorSerialNo": "FLDASTVENDORSERNO",
        "VendorWarrExp": "FLDASTVENDORWARREXP",
        "Version": "FLDASTVERSION",
        "WarrExpDate": "FLDASTWARREXPDATE"
    }

    def __init__(self, recid, crm_proxy=None):
        super().__init__(recid)
        self._crm_proxy = crm_proxy

class Charge(CRMEntity):
    db_fields = {
        "RecordID": "FLDSLPRECID",
        "ChargeSource": "FLDSLPSOURCERECID",
        "AccountRecID": "FLDSLPCARDID",
        "EmployeeRecID": "FLDSLPWORKERID",
        "ChargedItem": "FLDSLPITEMID",
        "ContractRecID": "FLDSLPBCRECID",
        "TicketRecID": "FLDSLPTICKETID",
        "Date": "FLDSLPSLIPDATE",
        "Description": "FLDSLPDESC",
        "Units": "FLDSLPQUANTITY",
        "AdjustAmount": "FLDSLPADJUSTAMOUNT",
        "AdjustPercent": "FLDSLPADJUSTPERCENT",
        "FromTime": "FLDSLPSTARTTIME",
        "ToTime": "FLDSLPENDTIME",
        "Price": "FLDSLPPRICE",
        "Billable": "FLDSLPBILLKIND",
        "Billed": "FLDSLPSTAGE",
        "Field1": "FLDSLPUSER1",
        "CreateUser": "FLDSLPCREATEUSER"
    }

    def __init__(self, recid, crm_proxy=None):
        super(__init__(recid, crm_proxy))

class HistoryNote(CRMEntity):
    db_fields = {
        "RecordID": "FLDHISRECID",
        "Date": "FLDHISNOTEDATETIME",
        "Description": "FLDHISDESCRIPTION",
        "LinkRecID": "FLDHISLINKRECID",
        "Field": "FLDHISUSER1",
        "About": "FLDHISKIND",
        "Employee": "FLDHISWORKERID",
        "Account": "FLDHISCARDID",
        "Contact": "FLDHISCONTACTID",
        "Document": "FLDHISDOCID",
        "CreatedByUser": "FLDHISCREATEUSER"
    }

    def __init__(self, recid, crm_proxy=None):
        super(__init__(recid, crm_proxy))

class Item(CRMEntity):
    db_fields = {
        "RecordID": "FLDITMRECID",
        "ItemGroup": "FLDITMITEMTYPEGROUP",
        "ItemCode": "FLDITMITEMNO",
        "ItemName": "FLDITMNAME",
        "PriceSource": "FLDITMPRICESOURCE",
        "PricePerUnit": "FLDITMUNITISHOUR",
        "Price": "FLDITMUNITPRICE",
        "Cost": "FLDITMSTANDARDCOST",
        "Taxes1": "FLDITMTAXCODE1",
        "Taxes2": "FLDITMTAXCODE2",
        "Taxes3": "FLDITMTAXCODE3",
        "DescByName": "FLDITMDESCBYNAME",
        "Description": "FLDITMDESC",
        "Suspend": "FLDITMSUSPENDED",
        "Notes": "FLDITMNOTES",
        "Field1": "FLDITMUSER1",
        "CreateUser": "FLDITMCREATEUSER",
        "CreatedByUSer": "FLDITMCREATEUSER"
    }

    def __init__(self, recid, crm_proxy=None):
        super(__init__(recid, crm_proxy))

class Ticket(CRMEntity):
    db_fields = {
        "AccountRecID": "FLDTKTCARDID",
        "ContactRecID": "FLDTKTCONTACTID",
        "ContractRecID": "FLDTKTBCRECID",
        "AssetRecID": "FLDTKTASSETRECID",
        "EmpRecID": "FLDTKTWORKERID",
        "Priority": "FLDTKTPRIORITY",
        "TicketNumber": "FLDTKTTICKETNO",
        "Description": "FLDTKTPROBLEM",
        "TicketType": "FLDTKTKIND",
        "Source": "FLDTKTSOURCE",
        "EstDuration": "FLDTKTSCHEDLENESTIM",
        "ShowTktInDisp": "FLDTKTFORDISPATCH",
        "Status": "FLDTKTSTATUS",
        "CreatedByUser": "FLDTKTCREATEUSER",
        "DueDate": "FLDTKTDUEDATETIME",
        "Resolution": "FLDTKTSOLUTION"
    }

    def __init__(self, recid, crm_proxy=None):
        super().__init__(recid, crm_proxy)

# legacy compatibility
Entity = CRMEntity.types
AccountFields = Account.db_fields
AssetFields = Asset.db_fields
ChargeFields = Charge.db_fields
HistoryNoteFields = HistoryNote.db_fields
ItemFields = Item.db_fields
TicketFields = Ticket.db_fields

if __name__ == '__main__':
    from xmlrpc.client import ServerProxy
    crm_proxy = ServerProxy('http://10.10.100.11:8000')
    acct = Account('CRDPX9UC9KOZB1ERMXUJ', crm_proxy)

    print(acct.db_data)
