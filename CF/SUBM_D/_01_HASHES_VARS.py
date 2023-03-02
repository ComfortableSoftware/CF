import base64 as B64
import hashlib as HL
import random as RND


V = None


ALLOWED_ALPHA_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALLOWED_CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
ALLOWED_HEX_CHARACTERS = "0123456789ABCDEF"
HASH_BLAKE2B = HL.blake2b()  # 64 byte fast hash
HASH_BLAKE2S = HL.blake2s()  # 32 byte fast hash
HASH_MD5 = HL.md5()  # 16 byte fastest hash, most likely to collide
HASH_SHA1 = HL.sha1()  # 20 byte hash
HASH_SHA224 = HL.sha224()  # 28 byte hash
HASH_SHA256 = HL.sha256()  # 32 byte hash
HASH_SHA3_224 = HL.sha3_224()  # 28 byte hash
HASH_SHA3_256 = HL.sha3_256()  # 32 byte hash
HASH_SHA3_384 = HL.sha3_384()  # 48 byte hash
HASH_SHA3_512 = HL.sha3_512()  # 64 byte hash
HASH_SHA384 = HL.sha384()  # 48 byte hash",),
HASH_SHA512 = HL.sha512()  # 64 byte hash",),


ALL_THE_HASHES = {
  "HASH_BLAKE2B": HASH_BLAKE2B,
  "HASH_BLAKE2S": HASH_BLAKE2S,
  "HASH_MD5": HASH_MD5,
  "HASH_SHA1": HASH_SHA1,
  "HASH_SHA224": HASH_SHA224,
  "HASH_SHA256": HASH_SHA256,
  "HASH_SHA3_224": HASH_SHA3_224,
  "HASH_SHA3_256": HASH_SHA3_256,
  "HASH_SHA3_384": HASH_SHA3_384,
  "HASH_SHA3_512": HASH_SHA3_512,
  "HASH_SHA384": HASH_SHA384,
  "HASH_SHA512": HASH_SHA512,
}


HASH_TO_STRING = {
  HASH_BLAKE2B: "blake2b",
  HASH_BLAKE2S: "blake2s",
  HASH_MD5: "md5",
  HASH_SHA1: "sha1",
  HASH_SHA224: "sha224",
  HASH_SHA256: "sha256",
  HASH_SHA3_224: "sha3_224",
  HASH_SHA3_256: "sha3_256",
  HASH_SHA3_384: "sha3_384",
  HASH_SHA3_512: "sha3_512",
  HASH_SHA384: "sha384",
  HASH_SHA512: "sha512",
}


STRING_TO_HASH = {
  "blake2b": HASH_BLAKE2B,
  "blake2s": HASH_BLAKE2S,
  "md5": HASH_MD5,
  "sha1": HASH_SHA1,
  "sha224": HASH_SHA224,
  "sha256": HASH_SHA256,
  "sha3_224": HASH_SHA3_224,
  "sha3_256": HASH_SHA3_256,
  "sha3_384": HASH_SHA3_384,
  "sha3_512": HASH_SHA3_512,
  "sha384": HASH_SHA384,
  "sha512": HASH_SHA512,
}


def returnHash(source_):
  if (
      (source_ in V.HASH_TO_STRING)
  ):
    return source_
  elif (
      (isinstance(source_, str) is True) and
      (source_.lower() in V.STRING_TO_HASH)
  ):
    return V.STRING_TO_HASH[source_]
  return None


def returnNewHash(hashID_):
  _THash_ = V.returnStrHash(hashID_)
  if (
      (_THash_ is None)
  ):
    return None
  return HL.new(_THash_)


def returnStrHash(source_):
  if (
      (isinstance(source_, str) is True) and
      (source_.lower() in V.STRING_TO_HASH)
  ):
    return source_
  elif (
      (isinstance(source_, str) is True) and
      (source_.lower() not in V.STRING_TO_HASH)
  ):
    return None
  return V.HASH_TO_STRING.get(source_, None)


ALL_THE_HASHES_DATA = {
  "ALLOWED_CHARACTERS": ALLOWED_CHARACTERS,
  "B64": B64,
  "HASH_TO_STRING": HASH_TO_STRING,
  "HL": HL,
  "RND": RND,
  "STRING_TO_HASH": STRING_TO_HASH,
}
ALL_THE_HASHES_DATA.update(ALL_THE_HASHES)
